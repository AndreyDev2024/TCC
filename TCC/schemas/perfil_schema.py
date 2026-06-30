from typing import Optional

from pydantic import BaseModel


class EditarPerfil(BaseModel):
    nome: Optional[str] = None
    email: Optional[str] = None
    nicho: Optional[str] = None
    setor: Optional[str] = None
    foto: Optional[str] = None


class AlterarSenha(BaseModel):
    senha_atual: str
    nova_senha: str
