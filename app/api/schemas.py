from datetime import date, time, datetime

from pydantic import BaseModel, ConfigDict
class CoinResponse(BaseModel):

    id: int

    coin_id: str

    symbol: str

    name: str

    current_price: float

    market_cap: int

    market_cap_rank: int

    total_volume: int

    price_change_percentage_24h: float

    circulating_supply: float

    last_updated: datetime

    date: date

    time: time

    hour: int

    weekday: str

    market_cap_category: str

    price_trend: str

    loaded_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )
    