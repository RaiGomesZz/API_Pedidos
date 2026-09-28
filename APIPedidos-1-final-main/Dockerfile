FROM python:3.13-slim

# Evita .pyc, garante logs em tempo real (stdout sem buffer) e acelera o pip
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

# curl é usado apenas pelo HEALTHCHECK do container.
# psycopg2-binary já traz o libpq embutido, então nenhuma lib de banco
# precisa ser instalada aqui — a imagem fica enxuta e o build, rápido.
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

# Copia primeiro o requirements.txt para aproveitar o cache de camadas do
# Docker: as dependências só são reinstaladas quando ele muda.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
COPY ./app ./app

# Executa como usuário não-root por segurança
RUN useradd --create-home --shell /bin/bash appuser \
    && chown -R appuser:appuser /app
USER appuser

EXPOSE 8000

# Healthcheck do próprio container, batendo no endpoint GET /health
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
