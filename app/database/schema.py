from datetime import datetime, UTC

from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    BigInteger,
    Date,
    Time,
    DateTime,
)

from app.database.connection import Base


class CryptoPrice(Base):

    __tablename__ = "crypto_prices"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    coin_id = Column(
        String(255),
        nullable=False,
        unique=True,
    )

    symbol = Column(
        String(30),
        nullable=False,
    )

    name = Column(
        String(255),
        nullable=False,
    )

    current_price = Column(Float)

    market_cap = Column(BigInteger)

    market_cap_rank = Column(Integer)

    total_volume = Column(BigInteger)

    price_change_percentage_24h = Column(Float)

    circulating_supply = Column(Float)

    last_updated = Column(DateTime(timezone=True))

    date = Column(Date)

    time = Column(Time)

    hour = Column(Integer)

    weekday = Column(String(20))

    market_cap_category = Column(String(30))

    price_trend = Column(String(20))

    loaded_at = Column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(UTC),
    )