from sqlalchemy.orm import Session
from app.models.pedido import Pedido
from app.schemas.pedido import PedidoCreate
from app.repositories.pedido_repository import PedidoRepository

class PedidoService:
    def __init__(self, db: Session):
        self.repository = PedidoRepository(db)

    def criar_pedido(self, pedido_data: PedidoCreate):
        valor_total = pedido_data.quantidade * pedido_data.valor_unitario
        
        novo_pedido = Pedido(
            cliente=pedido_data.cliente,
            produto=pedido_data.produto,
            quantidade=pedido_data.quantidade,
            valor_unitario=pedido_data.valor_unitario,
            valor_total=valor_total,
            status="CRIADO"
        )
        return self.repository.criar(novo_pedido)

    def obter_pedido(self, pedido_id: int):
        return self.repository.buscar_por_id(pedido_id)

    def listar_pedidos(self):
        return self.repository.listar_todos()

    def alterar_status(self, pedido_id: int, novo_status: str):
        pedido = self.repository.buscar_por_id(pedido_id)
        if not pedido:
            return None
        return self.repository.atualizar_status(pedido, novo_status)