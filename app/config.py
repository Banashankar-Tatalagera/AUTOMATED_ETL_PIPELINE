from dotenv import load_dotenv
import os

# Load variables from the .env file
load_dotenv()

# -----------------------------
# Database Configuration
# -----------------------------
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# -----------------------------
# API Configuration
# -----------------------------
API_BASE_URL = os.getenv("API_BASE_URL")
VS_CURRENCY = os.getenv("VS_CURRENCY")
PER_PAGE = int(os.getenv("PER_PAGE", "100"))
PAGE = int(os.getenv("PAGE", "1"))

VS_CURRENCY = os.getenv("VS_CURRENCY", "usd")

