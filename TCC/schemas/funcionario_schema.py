from pydantic import BaseModel
class CriarFuncionario(BaseModel):
    nome: str
    cpf: int
    email: str
    senha: str
    tipo: str
    setor: str