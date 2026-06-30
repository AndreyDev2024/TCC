from fastapi import APIRouter, Depends

from services.equipe_service import ver_demandas_da_equipe, ver_equipe, ver_produtividade
from utils.dependecies import usuario_logado


equipe_router = APIRouter(prefix="/equipe", tags=["Equipe"])


@equipe_router.get("")
async def equipe(usuario=Depends(usuario_logado)):
    return ver_equipe(usuario)


@equipe_router.get("/funcionarios")
async def listar_funcionarios(usuario=Depends(usuario_logado)):
    return ver_equipe(usuario)


@equipe_router.get("/demandas")
async def demandas_da_equipe(usuario=Depends(usuario_logado)):
    return ver_demandas_da_equipe(usuario)


@equipe_router.get("/produtividade")
async def produtividade(usuario=Depends(usuario_logado)):
    return ver_produtividade(usuario)
