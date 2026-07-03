import requests

BASE_URL = "http://127.0.0.1:8000"


def get_all_coins():

    response = requests.get(
        f"{BASE_URL}/coins",
        params={
            "limit": 100
        }
    )

    response.raise_for_status()

    return response.json()