from fastapi import HTTPException

from models.equipe_modelo import produtividade_por_funcionario
from models.relatorio_modelo import (
    contar_funcionarios,
    listar_demandas_pendentes,
    listar_demandas_por_status,
    metricas_gerais
)


def _empresa_id_do_usuario(usuario):
    if usuario.get("tipo_login") == "empresa":
        return usuario.get("id")
    return usuario.get("empresa_id")


def _pode_ver_relatorios(usuario):
    if usuario.get("tipo_login") == "empresa":
        return True
    return usuario.get("tipo_login") == "funcionario" and usuario.get("tipo") == "adm"


def _validar_acesso_relatorios(usuario):
    if not _pode_ver_relatorios(usuario):
        raise HTTPException(status_code=403, detail="Apenas empresa ou funcionario adm podem ver relatorios")


def demandas_concluidas(usuario):
    _validar_acesso_relatorios(usuario)
    return listar_demandas_por_status(_empresa_id_do_usuario(usuario), "concluida")


def demandas_pendentes(usuario):
    _validar_acesso_relatorios(usuario)
    return listar_demandas_pendentes(_empresa_id_do_usuario(usuario))


def quantidade_funcionarios(usuario):
    _validar_acesso_relatorios(usuario)
    return contar_funcionarios(_empresa_id_do_usuario(usuario))


def metricas(usuario):
    _validar_acesso_relatorios(usuario)
    empresa_id = _empresa_id_do_usuario(usuario)
    return {
        "gerais": metricas_gerais(empresa_id),
        "produtividade": produtividade_por_funcionario(empresa_id)
    }
