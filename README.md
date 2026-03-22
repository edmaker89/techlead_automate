# TeachLead Monorepo

TeachLead é uma base inicial para evolução de uma plataforma educacional, organizada como monorepo com separação explícita entre frontend, backend e infraestrutura. Este repositório prioriza escalabilidade arquitetural e experiência de desenvolvimento local previsível.

O foco desta etapa é scaffolding: aplicação React pronta, API FastAPI modular por feature, persistência PostgreSQL via Docker Compose, migrações com Alembic e padrões de qualidade (CI + lint/format/typecheck).

## Estrutura do monorepo

```text
.
├── apps/
│   ├── backend/
│   │   ├── alembic.ini
│   │   ├── pyproject.toml
│   │   ├── migrations/
│   │   └── src/teachlead/
│   │       ├── api/
│   │       ├── core/
│   │       ├── db/
│   │       ├── features/
│   │       └── main.py
│   └── frontend/
│       ├── src/
│       └── ...
├── infra/
│   └── docker/
├── docker-compose.yml
└── .env.example
```

- `apps/frontend`: Vite + React + TypeScript + Tailwind.
- `apps/backend`: FastAPI com app factory, lifespan, módulos por feature e Alembic.
- `infra/docker`: Dockerfiles para desenvolvimento.

## Requisitos

- Docker + Docker Compose
- Node.js 20+
- pnpm 9+ (compatível com npm)
- Python 3.13
- [uv](https://docs.astral.sh/uv/)

## Setup rápido (Docker Compose)

1. Copie variáveis de ambiente:

   ```bash
   cp .env.example .env
   ```

2. Suba tudo:

   ```bash
   docker compose up --build
   ```

3. Acesse:
   - Frontend: <http://localhost:5173>
   - Backend docs: <http://localhost:8000/docs>
   - Healthcheck: <http://localhost:8000/health>

## Rodar backend local (sem Docker)

```bash
cd apps/backend
cp ../../.env.example ../../.env  # se ainda não existir
uv sync
uv run alembic upgrade head
uv run uvicorn teachlead.main:create_app --factory --reload --host 0.0.0.0 --port 8000
```

## Rodar frontend local (sem Docker)

```bash
cd apps/frontend
pnpm install
pnpm dev
```

> Se preferir npm: `npm install` e `npm run dev`.

## Comandos úteis

### Docker

```bash
docker compose up --build
docker compose down
docker compose logs -f backend
docker compose exec backend uv run alembic upgrade head
```

### Backend (uv + Alembic)

```bash
cd apps/backend
uv sync
uv run ruff check .
uv run ruff format .
uv run mypy src
uv run alembic revision --autogenerate -m "describe change"
uv run alembic upgrade head
```

### Frontend

```bash
cd apps/frontend
pnpm install
pnpm lint
pnpm typecheck
pnpm build
```

## Arquitetura backend feature-based

Cada módulo em `src/teachlead/features/<nome_feature>` é autocontido e expõe seu próprio `APIRouter` via `router.py`, com contratos em `schemas.py` e lógica em `service.py` (quando necessário). O agregador `src/teachlead/api/router.py` inclui os routers das features e evita acoplamento no `main.py`.

### Como criar uma nova feature

1. Criar pasta `src/teachlead/features/nova_feature/`.
2. Adicionar `router.py`, `schemas.py` e (opcional) `service.py`.
3. Importar e incluir o router em `src/teachlead/api/router.py`.

## Lifespan do FastAPI

A aplicação usa `lifespan` (async context manager) para ações de startup/shutdown. No startup, ela realiza um `SELECT 1` no banco para validar conectividade; no shutdown, emite log de encerramento limpo.

## Qualidade e CI

- Backend: `ruff` (lint+format) + `mypy`.
- Frontend: `eslint` + `prettier` + `tsc`.
- CI (GitHub Actions): executa checks de backend e frontend a cada push/PR.

