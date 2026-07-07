import requests
import os

BASE_URL = os.getenv(
    "API_URL",
    "http://api:8000"
)
# BASE_URL = "http://127.0.0.1:8000"


def get_all_coins():

    response = requests.get(
        f"{BASE_URL}/coins",
        params={
            "limit": 100
        }
    )

    response.raise_for_status()

    return response.json()