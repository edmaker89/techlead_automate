from teachlead.features.health.schemas import HealthResponse


class HealthService:
    @staticmethod
    def check() -> HealthResponse:
        return HealthResponse(status="ok", service="teachlead-backend")
