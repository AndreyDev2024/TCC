from models.empresa_modelo import cadastrar_empresa, buscar_empresa_por_cnpj, buscar_empresa_por_email
from utils.criptografia_util import gerar_hash
from utils.validadores import validar_cnpj, validar_email, validar_senha
from fastapi import HTTPException


def criar_empresa(
    nome,
    cnpj,
    email,
    senha,
    nicho
):
    resultado_cpf = validar_cnpj(cnpj)
    if resultado_cpf != True:
        raise HTTPException(status_code=400, detail=resultado_cpf)
    resultado_senha = validar_senha(senha)
    if resultado_senha != True:
        raise HTTPException(status_code=400, detail= resultado_senha)
    resultado_email = validar_email(email)
    if resultado_email != True:
        raise HTTPException(status_code= 400, detail = resultado_email)
    
    empresa = buscar_empresa_por_cnpj(cnpj)
    if empresa:
        raise HTTPException(status_code=409, detail= 'CNPJ ja cadastrado!')
    empresa = buscar_empresa_por_email(email)
    if empresa:
        raise HTTPException(status_code= 409, detail= 'Email ja cadastrado!')
    
    senha_cripitografada = gerar_hash(senha)
    
    cadastrar_empresa(
        nome,
        cnpj,
        email,
        senha_cripitografada,
        nicho
    )
    return {'detail': f'Bem vindo {nome}, seu cadastro foi realizado com sucesso!'}
    