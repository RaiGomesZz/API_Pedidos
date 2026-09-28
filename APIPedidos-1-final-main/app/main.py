from fastapi import FastAPI
from app.database import engine, Base
from app.api import pedidos

# Cria as tabelas no banco de dados automaticamente (apenas para ambiente de desenvolvimento/estudo)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Pedidos")

# Inclui os endpoints de pedidos criados
app.include_router(pedidos.router)

@app.get("/health")
def health_check():
    return {"status": "ok"}