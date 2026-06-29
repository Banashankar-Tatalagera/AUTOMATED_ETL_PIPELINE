import pandas as pd

from app.logger import logger


def market_cap_category(cap):

    if cap >= 10_000_000_000:
        return "Large Cap"

    elif cap >= 2_000_000_000:
        return "Mid Cap"

    return "Small Cap"


def price_trend(change):

    if change > 0:
        return "Bullish"

    elif change < 0:
        return "Bearish"

    return "Neutral"


def engineer_features(df):

    df = df.copy()

    df["date"] = df["last_updated"].dt.date

    df["time"] = df["last_updated"].dt.time

    df["hour"] = df["last_updated"].dt.hour

    df["weekday"] = df["last_updated"].dt.day_name()

    df["market_cap_category"] = df["market_cap"].apply(
        market_cap_category
    )

    df["price_trend"] = df[
        "price_change_percentage_24h"
    ].apply(price_trend)

    logger.info("Feature engineering completed.")

    return df