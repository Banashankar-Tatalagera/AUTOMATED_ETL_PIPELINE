from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.api.routes.coins import router as coins_router
app = FastAPI(
    title="Crypto ETL API",
    description="Backend API for the Automated ETL Pipeline project.",
    version="1.0.0"
)

app.include_router(coins_router)

app.include_router(health_router)

