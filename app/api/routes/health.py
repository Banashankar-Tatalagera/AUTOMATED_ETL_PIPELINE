from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def health_check():

    return {
        "status": "healthy",
        "message": "Crypto ETL API is running."
    }
