from datetime import datetime, UTC

from app.database.connection import get_session
from app.database.schema import CryptoPrice
from app.logger import logger


def load_dataframe(df):

    session = get_session()

    logger.info("Database session started.")

    inserted = 0

    updated = 0

    try:

        for _, row in df.iterrows():

            existing_coin = (
                session.query(CryptoPrice)
                .filter_by(coin_id=row["id"])
                .first()
            )

            if existing_coin:

                existing_coin.symbol = row["symbol"]
                existing_coin.name = row["name"]
                existing_coin.current_price = row["current_price"]
                existing_coin.market_cap = row["market_cap"]
                existing_coin.market_cap_rank = row["market_cap_rank"]
                existing_coin.total_volume = row["total_volume"]
                existing_coin.price_change_percentage_24h = row["price_change_percentage_24h"]
                existing_coin.circulating_supply = row["circulating_supply"]
                existing_coin.last_updated = row["last_updated"]
                existing_coin.date = row["date"]
                existing_coin.time = row["time"]
                existing_coin.hour = row["hour"]
                existing_coin.weekday = row["weekday"]
                existing_coin.market_cap_category = row["market_cap_category"]
                existing_coin.price_trend = row["price_trend"]
                existing_coin.loaded_at = datetime.now(UTC)

                updated += 1

            else:

                coin = CryptoPrice(

                    coin_id=row["id"],

                    symbol=row["symbol"],

                    name=row["name"],

                    current_price=row["current_price"],

                    market_cap=row["market_cap"],

                    market_cap_rank=row["market_cap_rank"],

                    total_volume=row["total_volume"],

                    price_change_percentage_24h=row["price_change_percentage_24h"],

                    circulating_supply=row["circulating_supply"],

                    last_updated=row["last_updated"],

                    date=row["date"],

                    time=row["time"],

                    hour=row["hour"],

                    weekday=row["weekday"],

                    market_cap_category=row["market_cap_category"],

                    price_trend=row["price_trend"],

                    loaded_at=datetime.now(UTC),
                )

                session.add(coin)

                inserted += 1

        session.commit()

        logger.info(
            f"Inserted: {inserted} | Updated: {updated}"
        )

    except Exception as e:

        session.rollback()

        logger.error(f"Database Error: {e}")

        raise

    finally:

        session.close()

        logger.info("Database session closed.")