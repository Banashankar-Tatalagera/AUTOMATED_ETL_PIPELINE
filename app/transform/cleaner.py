import pandas as pd

from app.logger import logger


def clean_dataframe(df):

    df = df.copy()

    before = len(df)

    df = df.drop_duplicates()

    after = len(df)

    logger.info(
        f"Removed {before-after} duplicate rows."
    )

    missing = df.isnull().sum()

    logger.info(
        f"Missing Values:\n{missing}"
    )

    numeric_columns = df.select_dtypes(
        include="number"
    ).columns

    df[numeric_columns] = df[numeric_columns].fillna(0)

    object_columns = df.select_dtypes(
        include="object"
    ).columns

    df[object_columns] = df[object_columns].fillna(
        "Unknown"
    )

    df["last_updated"] = pd.to_datetime(
        df["last_updated"]
    )

    logger.info(
        f"Clean DataFrame Shape : {df.shape}"
    )

    return df