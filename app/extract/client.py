import requests


from app.config import (
    API_BASE_URL,
    VS_CURRENCY,
    PER_PAGE,
    PAGE
)

from app.logger import logger
session = requests.Session()

def build_url():
    return (
        f"{API_BASE_URL}/coins/markets"
        f"?vs_currency={VS_CURRENCY}"
        f"&per_page={PER_PAGE}"
        f"&page={PAGE}"
    )

def fetch_data():

    logger.info("Starting API request")

    url = build_url()

    try:

        response = session.get(
            url,
            timeout=10
        )

        logger.info(f"Status Code : {response.status_code}")

        response.raise_for_status()

        return response

    except requests.exceptions.RequestException as e:

        logger.error(f"API Request Failed : {e}")

        raise

