import pandas as pd

from app.logger import logger
COLUMNS = [
    "id",
    "symbol",
    "name",
    "current_price",
    "market_cap",
    "market_cap_rank",
    "total_volume",
    "price_change_percentage_24h",
    "circulating_supply",
    "last_updated"
]

def parse_to_dataframe(data):

    df = pd.DataFrame(data)

    missing = [col for col in COLUMNS if col not in df.columns]

    if missing:
        logger.error(f"Missing columns: {missing}")
        raise KeyError(f"Missing columns: {missing}")

    df = df[COLUMNS]

    logger.info(f"DataFrame Created : {df.shape}")

    return df
