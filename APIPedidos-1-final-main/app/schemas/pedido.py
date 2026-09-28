from pydantic import BaseModel
from datetime import datetime

class PedidoCreate(BaseModel):
    cliente: str
    produto: str
    quantidade: int
    valor_unitario: float

class PedidoUpdateStatus(BaseModel):
    status: str

class PedidoResponse(BaseModel):
    id: int
    cliente: str
    produto: str
    quantidade: int
    valor_unitario: float
    valor_total: float
    status: str
    data_criacao: datetime

    class Config:
        from_attributes = True