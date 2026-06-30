from typing import Optional

from pydantic import BaseModel


class CriarDemanda(BaseModel):
    titulo: str
    descricao: str
    setor: str
    cidade: Optional[str] = None
    funcionario_id: Optional[int] = None


class EditarDemanda(BaseModel):
    titulo: Optional[str] = None
    descricao: Optional[str] = None
    setor: Optional[str] = None
    cidade: Optional[str] = None
    funcionario_id: Optional[int] = None


class AtualizarStatusDemanda(BaseModel):
    status: str
