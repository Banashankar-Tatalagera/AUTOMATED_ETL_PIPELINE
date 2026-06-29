from app.logger import logger

from app.transform.cleaner import clean_dataframe
from app.transform.engineer import engineer_features


def run_transformation_pipeline(df):

    logger.info("Transformation pipeline started.")

    clean_df = clean_dataframe(df)

    transformed_df = engineer_features(clean_df)

    logger.info("Transformation pipeline completed.")

    return transformed_df