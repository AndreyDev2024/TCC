from pydantic import BaseModel

class CriarEmpresa(BaseModel):
    nome: str
    cnpj: str
    email: str
    senha: str
    nicho: str