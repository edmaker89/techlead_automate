FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --no-cache-dir uv

COPY apps/backend /app
RUN uv sync

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "teachlead.main:create_app", "--factory", "--reload", "--host", "0.0.0.0", "--port", "8000"]
