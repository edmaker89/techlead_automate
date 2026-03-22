.PHONY: up down logs backend-shell migrate frontend-dev backend-dev

up:
	docker compose up --build

down:
	docker compose down

logs:
	docker compose logs -f

backend-shell:
	docker compose exec backend bash

migrate:
	docker compose exec backend uv run alembic upgrade head

frontend-dev:
	cd apps/frontend && pnpm dev

backend-dev:
	cd apps/backend && uv run uvicorn teachlead.main:create_app --factory --reload --host 0.0.0.0 --port 8000
