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
    df = df[COLUMNS]
    logger.info(
    f"DataFrame Created : {df.shape}"
)
    return df
