from pydantic import BaseModel
class CriarFuncionario(BaseModel):
    nome: str
    cpf: str
    email: str
    senha: str
    tipo: str
    setor: str