from fastapi import APIRouter

from teachlead.features.health.schemas import HealthResponse
from teachlead.features.health.service import HealthService

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
def healthcheck() -> HealthResponse:
    return HealthService.check()
