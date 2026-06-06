from pydantic import BaseModel
class LogarFuncionario(BaseModel):   
    cpf: int
    senha: str
class LogarEmpresa(BaseModel):
    cnpj: int
    senha: str