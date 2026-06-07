from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from schemas.auth_schema import LogarFuncionario
from services.auth_service import loginFuncionario, loginEmpresa

auth_router = APIRouter(prefix='/auth', tags=['auth'])

@auth_router.post('/logar/funcionario')
async def logincomofuncionario(dados: LogarFuncionario):
    cpf = dados.cpf
    senha = dados.senha
    reusultado = loginFuncionario(cpf, senha)
    return reusultado

@auth_router.post('/logar/empresa')
async def logincomoempresa(form_data: OAuth2PasswordRequestForm = Depends()):
    cnpj = form_data.username
    senha = form_data.password
    resultado = loginEmpresa(cnpj, senha)
    return resultado