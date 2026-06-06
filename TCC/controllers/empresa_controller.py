from fastapi import APIRouter
from schemas.empresa_schema import CriarEmpresa
from services.empresa_service import criar_empresa

empresas_router = APIRouter(prefix='/empresas', tags=['Empresas'])

@empresas_router.post('/empresa/criar')
async def cadsastrarEMPRESA(dados: CriarEmpresa):
    resultado = criar_empresa(
        nome = dados.nome,
        cnpj = dados.cnpj,
        email = dados.email,
        senha = dados.senha,
        nicho = dados.nicho
    )
    return resultado