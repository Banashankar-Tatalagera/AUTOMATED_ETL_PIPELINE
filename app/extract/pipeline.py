from app.logger import logger

from app.extract.client import fetch_data
from app.extract.validator import validate_response
from app.extract.parser import parse_to_dataframe


def run_extraction_pipeline():

    logger.info("Extraction pipeline started.")

    response = fetch_data()

    data = validate_response(response)

    df = parse_to_dataframe(data)

    logger.info("Extraction pipeline completed.")

    return df