from fastapi import APIRouter, Depends

from services.relatorio_service import (
    demandas_concluidas,
    demandas_pendentes,
    metricas,
    quantidade_funcionarios
)
from utils.dependecies import usuario_logado


relatorios_router = APIRouter(prefix="/relatorios", tags=["Relatorios"])


@relatorios_router.get("/demandas-concluidas")
async def relatorio_demandas_concluidas(usuario=Depends(usuario_logado)):
    return demandas_concluidas(usuario)


@relatorios_router.get("/demandas-pendentes")
async def relatorio_demandas_pendentes(usuario=Depends(usuario_logado)):
    return demandas_pendentes(usuario)


@relatorios_router.get("/quantidade-funcionarios")
async def relatorio_quantidade_funcionarios(usuario=Depends(usuario_logado)):
    return quantidade_funcionarios(usuario)


@relatorios_router.get("/metricas")
async def relatorio_metricas(usuario=Depends(usuario_logado)):
    return metricas(usuario)
