import requests

from app.logger import logger

REQUIRED_FIELDS = [
    "id",
    "symbol",
    "name",
    "current_price",
    "market_cap",
    "total_volume",
    "last_updated"
]


def validate_response(response):

    if not isinstance(response, requests.models.Response):
        logger.error("Invalid response object.")
        raise TypeError("Expected a requests.Response object.")

    if response.status_code != 200:
        logger.error(f"Unexpected status code: {response.status_code}")
        raise ValueError("API request was unsuccessful.")

    content_type = response.headers.get("Content-Type", "")

    if "application/json" not in content_type:
        logger.error("Response is not JSON.")
        raise ValueError("Expected JSON response.")

    data = response.json()

    if not data:
        logger.warning("API returned empty data.")
        return data

    for field in REQUIRED_FIELDS:

        if field not in data[0]:
            logger.error(f"Missing field: {field}")
            raise KeyError(f"Missing field: {field}")

    logger.info("Response validation successful.")

    return data

