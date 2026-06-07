from models.funcionario_modelo import cadastrar_funcionario, buscar_funcionario_por_cpf, buscar_funcionario_por_email
from utils.validadores import validar_cpf, validar_senha, validar_email
from utils.criptografia_util import gerar_hash
from fastapi import HTTPException

def criar_funcionario(
    nome,
    cpf,
    email,
    senha,
    tipo,
    setor,
    empresa_id
):
    resultado_cpf = validar_cpf(cpf)
    if resultado_cpf != True:
        raise HTTPException(status_code=400, detail= resultado_cpf)
    
    resultado_senha = validar_senha(senha)
    if resultado_senha != True:
        raise HTTPException(status_code=400, detail= resultado_senha)
    
    resultado_email = validar_email(email)
    if resultado_email != True:
        raise HTTPException(status_code=400, detail= resultado_email)
    
    if tipo not in ["adm", "usuario"]:
        raise HTTPException(status_code=400, detail="Tipo deve ser 'adm' ou 'usuario'")
    
    funcionario = buscar_funcionario_por_cpf(cpf)
    if funcionario:
        raise HTTPException(status_code=409, detail= 'CPF ja registrado')
    
    funcionario = buscar_funcionario_por_email(email)
    if funcionario:
        raise HTTPException(status_code=409, detail= 'Email ja registrado')
    
    
    senha_ciptografada = gerar_hash(senha)
    
    cadastrar_funcionario(
        nome,
        cpf,
        email,
        senha_ciptografada,
        tipo,
        setor,
        empresa_id
        
    )
    return {"detail": f"Funcionário {nome} cadastrado com sucesso!"}