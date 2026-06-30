from fastapi import HTTPException

from models.equipe_modelo import (
    listar_demandas_da_equipe,
    listar_funcionarios_por_empresa,
    produtividade_por_funcionario
)


def _empresa_id_do_usuario(usuario):
    if usuario.get("tipo_login") == "empresa":
        return usuario.get("id")
    return usuario.get("empresa_id")


def _pode_ver_equipe(usuario):
    if usuario.get("tipo_login") == "empresa":
        return True
    return usuario.get("tipo_login") == "funcionario" and usuario.get("tipo") == "adm"


def _validar_acesso_equipe(usuario):
    if not _pode_ver_equipe(usuario):
        raise HTTPException(status_code=403, detail="Apenas empresa ou funcionario adm podem ver a equipe")


def ver_equipe(usuario):
    _validar_acesso_equipe(usuario)
    return listar_funcionarios_por_empresa(_empresa_id_do_usuario(usuario))


def ver_demandas_da_equipe(usuario):
    _validar_acesso_equipe(usuario)
    return listar_demandas_da_equipe(_empresa_id_do_usuario(usuario))


def ver_produtividade(usuario):
    _validar_acesso_equipe(usuario)
    return produtividade_por_funcionario(_empresa_id_do_usuario(usuario))
