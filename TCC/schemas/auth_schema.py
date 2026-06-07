from pydantic import BaseModel
class LogarFuncionario(BaseModel):   
    cpf: str
    senha: str
class LogarEmpresa(BaseModel):
    cnpj: str
    senha: str