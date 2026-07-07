from app.logger import logger

from app.extract.pipeline import run_extraction_pipeline
from app.transform.pipeline import run_transformation_pipeline
from app.load.loader import load_dataframe


def run_pipeline():

    logger.info("=" * 50)
    logger.info("Starting Complete ETL Pipeline")
    logger.info("=" * 50)

    # Extract
    extracted_df = run_extraction_pipeline()

    # Transform
    transformed_df = run_transformation_pipeline(
        extracted_df
    )

    # Load
    load_dataframe(
        transformed_df
    )

    logger.info("=" * 50)
    logger.info("ETL Pipeline Completed Successfully")
    logger.info("=" * 50)


if __name__ == "__main__":
    run_pipeline()