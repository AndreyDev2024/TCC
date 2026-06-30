from fastapi import HTTPException

from models.demanda_modelo import (
    atualizar_status_demanda,
    buscar_demanda_por_id,
    cadastrar_demanda,
    editar_demanda,
    listar_demandas
)
from models.historico_modelo import listar_historico_por_demanda, registrar_historico_demanda


STATUS_VALIDOS = ["aberta", "em_andamento", "concluida", "cancelada"]


def _empresa_id_do_usuario(usuario):
    if usuario.get("tipo_login") == "empresa":
        return usuario.get("id")
    return usuario.get("empresa_id")


def _pode_gerenciar(usuario):
    if usuario.get("tipo_login") == "empresa":
        return True
    return usuario.get("tipo_login") == "funcionario" and usuario.get("tipo") == "adm"


def _usuario_id(usuario):
    return usuario.get("id")


def _registrar_log(demanda_id, usuario, acao, descricao):
    registrar_historico_demanda(
        demanda_id=demanda_id,
        usuario_tipo=usuario.get("tipo_login"),
        usuario_id=_usuario_id(usuario),
        acao=acao,
        descricao=descricao
    )


def _validar_status(status):
    if status not in STATUS_VALIDOS:
        raise HTTPException(
            status_code=400,
            detail="Status deve ser: aberta, em_andamento, concluida ou cancelada"
        )


def _buscar_demanda_da_empresa(demanda_id, usuario):
    demanda = buscar_demanda_por_id(demanda_id)
    if not demanda:
        raise HTTPException(status_code=404, detail="Demanda nao encontrada")

    if demanda["empresa_id"] != _empresa_id_do_usuario(usuario):
        raise HTTPException(status_code=403, detail="Demanda pertence a outra empresa")

    return demanda


def criar_demanda(dados, usuario):
    if not _pode_gerenciar(usuario):
        raise HTTPException(status_code=403, detail="Apenas empresa ou funcionario adm podem criar demandas")

    demanda_id = cadastrar_demanda(
        titulo=dados.titulo,
        descricao=dados.descricao,
        status="aberta",
        setor=dados.setor,
        cidade=dados.cidade,
        empresa_id=_empresa_id_do_usuario(usuario),
        funcionario_id=dados.funcionario_id
    )
    _registrar_log(
        demanda_id,
        usuario,
        "criacao",
        f"Demanda '{dados.titulo}' criada"
    )

    return {
        "detail": "Demanda criada com sucesso",
        "id_demanda": demanda_id
    }


def listar_demandas_service(setor, status, funcionario_id, cidade, usuario):
    if status:
        _validar_status(status)

    empresa_id = _empresa_id_do_usuario(usuario)

    if usuario.get("tipo_login") == "funcionario" and usuario.get("tipo") == "usuario":
        funcionario_id = usuario.get("id")

    return listar_demandas(
        empresa_id=empresa_id,
        setor=setor,
        status=status,
        funcionario_id=funcionario_id,
        cidade=cidade
    )


def buscar_demanda_service(demanda_id, usuario):
    demanda = _buscar_demanda_da_empresa(demanda_id, usuario)

    if usuario.get("tipo_login") == "funcionario" and usuario.get("tipo") == "usuario":
        if demanda["funcionario_id"] != usuario.get("id"):
            raise HTTPException(status_code=403, detail="Voce so pode ver suas proprias demandas")

    return demanda


def editar_demanda_service(demanda_id, dados, usuario):
    if not _pode_gerenciar(usuario):
        raise HTTPException(status_code=403, detail="Apenas empresa ou funcionario adm podem editar demandas")

    _buscar_demanda_da_empresa(demanda_id, usuario)

    campos = {}
    alteracoes = []
    if dados.titulo is not None:
        campos["titulo_demanda"] = dados.titulo
        alteracoes.append("titulo")
    if dados.descricao is not None:
        campos["descricao_demanda"] = dados.descricao
        alteracoes.append("descricao")
    if dados.setor is not None:
        campos["setor_demanda"] = dados.setor
        alteracoes.append("setor")
    if dados.cidade is not None:
        campos["cidade_demanda"] = dados.cidade
        alteracoes.append("cidade")
    if dados.funcionario_id is not None:
        campos["funcionario_id"] = dados.funcionario_id
        alteracoes.append("funcionario responsavel")

    if not campos:
        raise HTTPException(status_code=400, detail="Nenhum campo enviado para edicao")

    editar_demanda(demanda_id, campos)
    _registrar_log(
        demanda_id,
        usuario,
        "edicao",
        f"Campos alterados: {', '.join(alteracoes)}"
    )
    return {"detail": "Demanda editada com sucesso"}


def atualizar_status_demanda_service(demanda_id, status, usuario):
    _validar_status(status)
    demanda = _buscar_demanda_da_empresa(demanda_id, usuario)

    if not _pode_gerenciar(usuario):
        if demanda["funcionario_id"] != usuario.get("id"):
            raise HTTPException(status_code=403, detail="Voce so pode atualizar suas proprias demandas")

    atualizar_status_demanda(demanda_id, status)
    _registrar_log(
        demanda_id,
        usuario,
        "alteracao_status",
        f"Status alterado para {status}"
    )
    return {"detail": "Status da demanda atualizado com sucesso"}


def cancelar_demanda_service(demanda_id, usuario):
    if not _pode_gerenciar(usuario):
        raise HTTPException(status_code=403, detail="Apenas empresa ou funcionario adm podem cancelar demandas")

    _buscar_demanda_da_empresa(demanda_id, usuario)
    atualizar_status_demanda(demanda_id, "cancelada")
    _registrar_log(
        demanda_id,
        usuario,
        "cancelamento",
        "Demanda cancelada"
    )
    return {"detail": "Demanda cancelada com sucesso"}


def listar_historico_demanda_service(demanda_id, usuario):
    if not _pode_gerenciar(usuario):
        raise HTTPException(status_code=403, detail="Apenas empresa ou funcionario adm podem ver o historico")

    _buscar_demanda_da_empresa(demanda_id, usuario)
    return listar_historico_por_demanda(demanda_id)
