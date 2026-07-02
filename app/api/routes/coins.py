from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.api.schemas import CoinResponse
from app.database.schema import CryptoPrice

router = APIRouter(
    prefix="/coins",
    tags=["Coins"]
)


# -------------------------------------------------------------------
# Get all coins
# -------------------------------------------------------------------
@router.get(
    "/",
    response_model=list[CoinResponse]
)
@router.get(
    "/",
    response_model=list[CoinResponse]
)
@router.get(
    "/",
    response_model=list[CoinResponse]
)
def get_all_coins(
    limit: int = Query(default=20, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    sort_by: str = Query(default="market_cap_rank"),
    order: str = Query(default="asc", pattern="^(asc|desc)$"),
    db: Session = Depends(get_db)
):

    allowed_columns = {
        "coin_id": CryptoPrice.coin_id,
        "name": CryptoPrice.name,
        "current_price": CryptoPrice.current_price,
        "market_cap": CryptoPrice.market_cap,
        "market_cap_rank": CryptoPrice.market_cap_rank,
        "total_volume": CryptoPrice.total_volume,
        "last_updated": CryptoPrice.last_updated,
    }

    column = allowed_columns.get(sort_by)

    if column is None:

        raise HTTPException(
            status_code=400,
            detail="Invalid sort field."
        )

    if order == "desc":
        column = column.desc()
    else:
        column = column.asc()

    return (
        db.query(CryptoPrice)
        .order_by(column)
        .offset(offset)
        .limit(limit)
        .all()
    )


# -------------------------------------------------------------------
# Top 10 coins by Market Cap
# -------------------------------------------------------------------
@router.get(
    "/top10",
    response_model=list[CoinResponse]
)
def get_top10(
    db: Session = Depends(get_db)
):

    return (
        db.query(CryptoPrice)
        .order_by(CryptoPrice.market_cap.desc())
        .limit(10)
        .all()
    )


# -------------------------------------------------------------------
# Bullish Coins
# -------------------------------------------------------------------
@router.get(
    "/bullish",
    response_model=list[CoinResponse]
)
def get_bullish_coins(
    db: Session = Depends(get_db)
):

    return (
        db.query(CryptoPrice)
        .filter(CryptoPrice.price_trend == "Bullish")
        .all()
    )


# -------------------------------------------------------------------
# Bearish Coins
# -------------------------------------------------------------------
@router.get(
    "/bearish",
    response_model=list[CoinResponse]
)
def get_bearish_coins(
    db: Session = Depends(get_db)
):

    return (
        db.query(CryptoPrice)
        .filter(CryptoPrice.price_trend == "Bearish")
        .all()
    )


# -------------------------------------------------------------------
# Search Coins
# Example:
# /coins/search?name=bit
# -------------------------------------------------------------------
@router.get(
    "/search",
    response_model=list[CoinResponse]
)
def search_coin(
    name: str = Query(...),
    db: Session = Depends(get_db)
):

    return (
        db.query(CryptoPrice)
        .filter(CryptoPrice.name.ilike(f"%{name}%"))
        .all()
    )


# -------------------------------------------------------------------
# Coins by Market Cap Category
# Example:
# /coins/category/Large%20Cap
# -------------------------------------------------------------------
@router.get(
    "/category/{category}",
    response_model=list[CoinResponse]
)
def get_market_cap_category(
    category: str,
    db: Session = Depends(get_db)
):

    return (
        db.query(CryptoPrice)
        .filter(CryptoPrice.market_cap_category == category)
        .all()
    )


# -------------------------------------------------------------------
# Get Single Coin
# -------------------------------------------------------------------
@router.get(
    "/{coin_id}",
    response_model=CoinResponse
)
def get_coin(
    coin_id: str,
    db: Session = Depends(get_db)
):

    coin = (
        db.query(CryptoPrice)
        .filter(CryptoPrice.coin_id == coin_id)
        .first()
    )

    if coin is None:
        raise HTTPException(
            status_code=404,
            detail="Coin not found."
        )

    return coin