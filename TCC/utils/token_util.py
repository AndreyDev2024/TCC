from jose import jwt
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
import os

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')
)
def criar_access_token(dados:dict):
    dados_token = dados.copy()
    expiracao = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )
    dados_token.update({
        'exp':expiracao
    })
    token = jwt.encode(
        dados_token,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    return token