import streamlit as st
import pandas as pd

from api_client import get_all_coins
from charts import (
    market_cap_chart,
    trend_chart,
    category_chart
)

st.set_page_config(
    page_title="Crypto ETL Dashboard",
    page_icon="📈",
    layout="wide"
)

# ==============================
# Load Data
# ==============================

coins = get_all_coins()
df = pd.DataFrame(coins)

# ==============================
# Dashboard Title
# ==============================

st.title("📈 Crypto ETL Dashboard")

# ==============================
# KPI Calculations
# ==============================

total = len(df)

bullish = len(df[df["price_trend"] == "Bullish"])

bearish = len(df[df["price_trend"] == "Bearish"])

large_cap = len(df[df["market_cap_category"] == "Large Cap"])

# ==============================
# KPI Cards
# ==============================

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Coins", total)
col2.metric("Bullish", bullish)
col3.metric("Bearish", bearish)
col4.metric("Large Cap", large_cap)

st.divider()

# ==============================
# Search
# ==============================

search = st.text_input(
    "🔍 Search Coin",
    placeholder="Bitcoin, Ethereum..."
)

if search:
    df = df[
        df["name"].str.contains(search, case=False)
    ]

# ==============================
# Charts
# ==============================

left, right = st.columns(2)

with left:
    st.plotly_chart(
        market_cap_chart(df),
        use_container_width=True
    )

with right:
    st.plotly_chart(
        trend_chart(df),
        use_container_width=True
    )

st.plotly_chart(
    category_chart(df),
    use_container_width=True
)

st.divider()

# ==============================
# Table
# ==============================

st.subheader("Coin Data")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)