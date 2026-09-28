from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schemas.pedido import PedidoCreate, PedidoResponse, PedidoUpdateStatus
from app.services.pedido_service import PedidoService

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])

@router.post("/", response_model=PedidoResponse, status_code=status.HTTP_201_CREATED)
def criar_pedido(pedido: PedidoCreate, db: Session = Depends(get_db)):
    service = PedidoService(db)
    return service.criar_pedido(pedido)

@router.get("/{id}", response_model=PedidoResponse)
def consultar_pedido(id: int, db: Session = Depends(get_db)):
    service = PedidoService(db)
    pedido = service.obter_pedido(id)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    return pedido

@router.get("/", response_model=List[PedidoResponse])
def listar_pedidos(db: Session = Depends(get_db)):
    service = PedidoService(db)
    return service.listar_pedidos()

@router.patch("/{id}/status", response_model=PedidoResponse)
def alterar_status(id: int, status_update: PedidoUpdateStatus, db: Session = Depends(get_db)):
    service = PedidoService(db)
    pedido_atualizado = service.alterar_status(id, status_update.status)
    if not pedido_atualizado:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    return pedido_atualizado