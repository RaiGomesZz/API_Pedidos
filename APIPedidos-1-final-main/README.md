# API de Pedidos — Trabalho 1

API REST para gerenciamento de pedidos, desenvolvida em **FastAPI** com
persistência em **PostgreSQL**, totalmente containerizada com **Docker
Compose**.

> **Status atual:** infraestrutura base validada via `GET /health`. As
> regras de negócio do recurso `/pedidos` ainda serão implementadas.

## Stack

- Python 3.13 + FastAPI
- PostgreSQL 18
- SQLAlchemy 2.0
- Docker + Docker Compose

## Como executar

Pré-requisito: apenas **Docker** e **Docker Compose**. Nenhuma outra
dependência precisa estar instalada localmente.

```bash
docker compose up -d --build
```

Esse comando sobe dois serviços, sem nenhum passo manual adicional:

- `pedidos` — API FastAPI, disponível em http://localhost:8000
- `postgres` — banco de dados PostgreSQL, com os dados persistidos no
  volume `postgres_data`

## Testar

```bash
curl http://localhost:8000/health
# {"status":"ok"}
```

Documentação interativa (Swagger UI): http://localhost:8000/docs

## Variáveis de ambiente

Veja `.env.example`. Os valores padrão já estão configurados no
`docker-compose.yml`, então copiar para `.env` é **opcional** — só é
necessário se você quiser customizar usuário/senha/nome do banco.

## Estrutura do projeto

```
app/
├── main.py         # inicialização do FastAPI
├── api/            # endpoints HTTP (routers)
├── services/       # regras de negócio da aplicação
├── repositories/   # abstração de acesso e persistência de dados
├── models/         # modelos ORM (SQLAlchemy)
└── schemas/        # schemas de entrada/saída da API (Pydantic)
```

## Parar a aplicação

```bash
docker compose down        # para os containers, mantém os dados
docker compose down -v     # para os containers e apaga o volume do banco
```

## Logs

```bash
docker compose logs -f pedidos     # logs só da API
docker compose logs -f             # logs de todos os serviços
```
