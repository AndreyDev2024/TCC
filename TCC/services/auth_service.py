#FUNCIONARIO
from models.funcionario_modelo import buscar_funcionario_por_cpf

#EMPRESA
from models.empresa_modelo import buscar_empresa_por_cnpj

#UTILITARIOS
from utils.criptografia_util import verificar_senha
from utils.token_util import criar_access_token

#IMPORTS
from fastapi import HTTPException


def loginFuncionario(cpf,senha):
    
    funcionario = buscar_funcionario_por_cpf(cpf)
    
    if not funcionario:
        raise HTTPException(status_code=404, detail= 'Sem funcionarios registrado!')
    if not verificar_senha(
        senha,
        funcionario[4]
    ):
        raise HTTPException(status_code= 401, detail= 'Senha incorreta, tente novamente!')
    access_token = criar_access_token({
        'id': funcionario[0],
        'nome': funcionario[1],
        'tipo': funcionario[5],
        'setor': funcionario[6]
    })
    return{
        'mensagem': f'Bem vindo {funcionario[1]}',
        'access token': access_token,
        'token type': 'Bearer'
    }
def loginEmpresa(cnpj,senha):
    empresa = buscar_empresa_por_cnpj(cnpj)
    if not empresa:
        raise HTTPException(status_code=404, detail= 'Sem empresas cadastradas!')
    if not verificar_senha(
        senha,
        empresa[4]
    ):
        raise HTTPException(status_code=401, detail= 'SSenha incorreta, tente novamente!')
    access_token = criar_access_token({
        'id': empresa[0],
        'nome': empresa[1],
        'nicho': empresa[4]
    })
    return{ 'mensagem': f'Bem vindo {empresa[1]}',
           'access token' : access_token,
           'token type': 'Bearer' 
    }