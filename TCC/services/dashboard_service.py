from fastapi import HTTPException

from models.equipe_modelo import produtividade_por_funcionario
from models.relatorio_modelo import contar_funcionarios, metricas_gerais


def _empresa_id_do_usuario(usuario):
    if usuario.get("tipo_login") == "empresa":
        return usuario.get("id")
    return usuario.get("empresa_id")


def _pode_ver_dashboard(usuario):
    if usuario.get("tipo_login") == "empresa":
        return True
    return usuario.get("tipo_login") == "funcionario" and usuario.get("tipo") == "adm"


def dashboard(usuario):
    if not _pode_ver_dashboard(usuario):
        raise HTTPException(status_code=403, detail="Apenas empresa ou funcionario adm podem ver o dashboard")

    empresa_id = _empresa_id_do_usuario(usuario)
    metricas = metricas_gerais(empresa_id)
    funcionarios = contar_funcionarios(empresa_id)
    produtividade = produtividade_por_funcionario(empresa_id)

    return {
        "estatisticas": metricas,
        "cards": {
            "total_demandas": metricas["total_demandas"],
            "demandas_concluidas": metricas["concluidas"],
            "demandas_pendentes": metricas["abertas"] + metricas["em_andamento"],
            "quantidade_funcionarios": funcionarios["quantidade_funcionarios"]
        },
        "numeros": {
            "abertas": metricas["abertas"],
            "em_andamento": metricas["em_andamento"],
            "concluidas": metricas["concluidas"],
            "canceladas": metricas["canceladas"]
        },
        "indicadores": {
            "percentual_conclusao": metricas["percentual_conclusao"],
            "produtividade_por_funcionario": produtividade
        }
    }
