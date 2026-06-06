from pydantic import BaseModel

class CriarEmpresa(BaseModel):
    nome: str
    cnpj: int
    email: str
    senha: str
    nicho: str