from typing import Optional

from fastapi import APIRouter, Depends

from schemas.demanda_schema import AtualizarStatusDemanda, CriarDemanda, EditarDemanda
from services.demanda_service import (
    atualizar_status_demanda_service,
    buscar_demanda_service,
    cancelar_demanda_service,
    criar_demanda,
    editar_demanda_service,
    listar_historico_demanda_service,
    listar_demandas_service
)
from utils.dependecies import usuario_logado


demandas_router = APIRouter(prefix="/demandas", tags=["Demandas"])


@demandas_router.post("/criar")
async def criar(dados: CriarDemanda, usuario=Depends(usuario_logado)):
    return criar_demanda(dados, usuario)


@demandas_router.get("")
async def listar(
    setor: Optional[str] = None,
    status: Optional[str] = None,
    funcionario_id: Optional[int] = None,
    cidade: Optional[str] = None,
    usuario=Depends(usuario_logado)
):
    return listar_demandas_service(setor, status, funcionario_id, cidade, usuario)


@demandas_router.get("/{demanda_id}")
async def buscar(demanda_id: int, usuario=Depends(usuario_logado)):
    return buscar_demanda_service(demanda_id, usuario)


@demandas_router.get("/{demanda_id}/historico")
async def listar_historico(demanda_id: int, usuario=Depends(usuario_logado)):
    return listar_historico_demanda_service(demanda_id, usuario)


@demandas_router.put("/{demanda_id}")
async def editar(demanda_id: int, dados: EditarDemanda, usuario=Depends(usuario_logado)):
    return editar_demanda_service(demanda_id, dados, usuario)


@demandas_router.patch("/{demanda_id}/status")
async def atualizar_status(
    demanda_id: int,
    dados: AtualizarStatusDemanda,
    usuario=Depends(usuario_logado)
):
    return atualizar_status_demanda_service(demanda_id, dados.status, usuario)


@demandas_router.delete("/{demanda_id}")
async def deletar(demanda_id: int, usuario=Depends(usuario_logado)):
    return cancelar_demanda_service(demanda_id, usuario)
