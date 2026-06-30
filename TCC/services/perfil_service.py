from fastapi import HTTPException

from models.perfil_modelo import (
    atualizar_empresa,
    atualizar_funcionario,
    buscar_empresa_com_senha,
    buscar_empresa_por_email,
    buscar_funcionario_com_senha,
    buscar_funcionario_por_email,
    buscar_perfil_empresa,
    buscar_perfil_funcionario
)
from utils.criptografia_util import gerar_hash, verificar_senha
from utils.validadores import validar_email, validar_senha


def ver_perfil(usuario):
    if usuario.get("tipo_login") == "empresa":
        perfil = buscar_perfil_empresa(usuario.get("id"))
    else:
        perfil = buscar_perfil_funcionario(usuario.get("id"))

    if not perfil:
        raise HTTPException(status_code=404, detail="Perfil nao encontrado")

    return perfil


def editar_perfil(dados, usuario):
    if usuario.get("tipo_login") == "empresa":
        return _editar_empresa(dados, usuario.get("id"))
    return _editar_funcionario(dados, usuario.get("id"))


def _editar_empresa(dados, empresa_id):
    campos = {}

    if dados.nome is not None:
        campos["nome_empresa"] = dados.nome
    if dados.email is not None:
        _validar_email_unico_empresa(dados.email, empresa_id)
        campos["email_empresa"] = dados.email
    if dados.nicho is not None:
        campos["nicho_empresa"] = dados.nicho
    if dados.foto is not None:
        campos["foto_empresa"] = dados.foto

    if dados.setor is not None:
        raise HTTPException(status_code=400, detail="Empresa nao possui setor")

    if not campos:
        raise HTTPException(status_code=400, detail="Nenhum campo enviado para edicao")

    atualizar_empresa(empresa_id, campos)
    return {"detail": "Perfil da empresa atualizado com sucesso"}


def _editar_funcionario(dados, funcionario_id):
    campos = {}

    if dados.nome is not None:
        campos["nome_funcionario"] = dados.nome
    if dados.email is not None:
        _validar_email_unico_funcionario(dados.email, funcionario_id)
        campos["email_funcionario"] = dados.email
    if dados.setor is not None:
        campos["setor_funcionario"] = dados.setor
    if dados.foto is not None:
        campos["foto_funcionario"] = dados.foto

    if dados.nicho is not None:
        raise HTTPException(status_code=400, detail="Funcionario nao possui nicho")

    if not campos:
        raise HTTPException(status_code=400, detail="Nenhum campo enviado para edicao")

    atualizar_funcionario(funcionario_id, campos)
    return {"detail": "Perfil do funcionario atualizado com sucesso"}


def alterar_senha(dados, usuario):
    resultado_senha = validar_senha(dados.nova_senha)
    if resultado_senha != True:
        raise HTTPException(status_code=400, detail=resultado_senha)

    if usuario.get("tipo_login") == "empresa":
        empresa = buscar_empresa_com_senha(usuario.get("id"))
        if not empresa:
            raise HTTPException(status_code=404, detail="Empresa nao encontrada")
        if not verificar_senha(dados.senha_atual, empresa["senha_empresa"]):
            raise HTTPException(status_code=401, detail="Senha atual incorreta")

        atualizar_empresa(usuario.get("id"), {"senha_empresa": gerar_hash(dados.nova_senha)})
        return {"detail": "Senha da empresa alterada com sucesso"}

    funcionario = buscar_funcionario_com_senha(usuario.get("id"))
    if not funcionario:
        raise HTTPException(status_code=404, detail="Funcionario nao encontrado")
    if not verificar_senha(dados.senha_atual, funcionario["senha_funcionario"]):
        raise HTTPException(status_code=401, detail="Senha atual incorreta")

    atualizar_funcionario(usuario.get("id"), {"senha_funcionario": gerar_hash(dados.nova_senha)})
    return {"detail": "Senha do funcionario alterada com sucesso"}


def _validar_email_unico_empresa(email, empresa_id):
    resultado_email = validar_email(email)
    if resultado_email != True:
        raise HTTPException(status_code=400, detail=resultado_email)

    empresa = buscar_empresa_por_email(email)
    if empresa and empresa["id_empresa"] != empresa_id:
        raise HTTPException(status_code=409, detail="Email ja cadastrado")


def _validar_email_unico_funcionario(email, funcionario_id):
    resultado_email = validar_email(email)
    if resultado_email != True:
        raise HTTPException(status_code=400, detail=resultado_email)

    funcionario = buscar_funcionario_por_email(email)
    if funcionario and funcionario["id_funcionario"] != funcionario_id:
        raise HTTPException(status_code=409, detail="Email ja cadastrado")
