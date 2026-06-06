from fastapi import APIRouter

from schemas.auth_schema import LogarFuncionario, LogarEmpresa
from services.auth_service import loginFuncionario, loginEmpresa

auth_router = APIRouter(prefix='/auth', tags=['auth'])

@auth_router.post('/logar/funcionario')
async def logincomofuncionario(dados: LogarFuncionario):
    cpf = dados.cpf
    senha = dados.senha
    reusultado = loginFuncionario(cpf, senha)
    return reusultado

@auth_router.post('/logar/empresa')
async def logincomoempresa(dados: LogarEmpresa):
    cnpj = dados.cnpj
    senha = dados.senha
    resultado = loginEmpresa(cnpj,senha)
    return resultado