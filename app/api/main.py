from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.api.routes.coins import router as coins_router
from app.database.connection import engine
from app.database.schema import Base


app = FastAPI(
    title="Crypto ETL API",
    description="Backend API for the Automated ETL Pipeline project.",
    version="1.0.0"
)


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


app.include_router(coins_router)
app.include_router(health_router)