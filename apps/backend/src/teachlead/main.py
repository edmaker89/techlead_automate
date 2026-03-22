from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

from teachlead.api.router import api_router
from teachlead.core.config import get_settings
from teachlead.core.logging import configure_logging
from teachlead.db.session import SessionLocal


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncIterator[None]:
    settings = get_settings()
    configure_logging(settings.log_level)

    with SessionLocal() as session:
        session.execute(text("SELECT 1"))

    yield


def create_app() -> FastAPI:
    settings = get_settings()

    app = FastAPI(
        title="TeachLead API",
        version="0.1.0",
        lifespan=lifespan,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(api_router)
    return app


app = create_app()
