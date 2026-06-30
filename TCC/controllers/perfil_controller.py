from fastapi import APIRouter, Depends

from schemas.perfil_schema import AlterarSenha, EditarPerfil
from services.perfil_service import alterar_senha, editar_perfil, ver_perfil
from utils.dependecies import usuario_logado


perfil_router = APIRouter(prefix="/perfil", tags=["Perfil"])


@perfil_router.get("")
async def buscar_perfil(usuario=Depends(usuario_logado)):
    return ver_perfil(usuario)


@perfil_router.put("")
async def atualizar_perfil(dados: EditarPerfil, usuario=Depends(usuario_logado)):
    return editar_perfil(dados, usuario)


@perfil_router.patch("/senha")
async def atualizar_senha(dados: AlterarSenha, usuario=Depends(usuario_logado)):
    return alterar_senha(dados, usuario)
