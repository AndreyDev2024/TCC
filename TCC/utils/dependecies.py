from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
oauth2_schema = OAuth2PasswordBearer(
    tokenUrl= "/auth/logar/empresa"
)
def pegar_empresa_logado(token: str = Depends(oauth2_schema)):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail= 'Token invalido ou expirado')
    
def empresa_logada(usuario = Depends(pegar_empresa_logado)):
    if usuario.get('tipo_login') != 'empresa':
        raise HTTPException(
            status_code=403,
            detail='Apenas empresas podem fazer essa funcao'
        )
    return usuario

def funcionario_logado(usuario = Depends(pegar_empresa_logado)):
    if usuario.get('tipo_login') != 'funcionario':
        raise HTTPException(status_code=403, detail='Apenas usuarios podem utilizar essa funcao')
    
def admin_logado(usuario = Depends(funcionario_logado)):
    if usuario.get("tipo") != "adm":
        raise HTTPException(status_code=403, detail="Apenas administradores")
    return usuario