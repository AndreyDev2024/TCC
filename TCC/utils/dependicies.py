from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from dotenv import load_dotenv
import os

load_dotenv

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHIM = os.getenv('ALGORITHM')
oauth2_schema = OAuth2PasswordBearer(
    tokenurl= "/auth/logar/funcioanrio"
)
def pegar_usuario_logado(token: str = Depends(oauth2_schema)):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=['ALGORITHM']
        )
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail= 'Token invalido ou expirado')
    