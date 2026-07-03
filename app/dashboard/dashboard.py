import streamlit as st
import pandas as pd

from api_client import get_all_coins

from sidebar import sidebar_filters
from metrics import show_metrics
from charts import (
    market_cap_chart,
    trend_chart,
    category_chart
)
from details import show_details
from table import show_table


# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="Crypto ETL Dashboard",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Crypto ETL Dashboard")


# ==========================================
# Load Data
# ==========================================

coins = get_all_coins()
df = pd.DataFrame(coins)


# ==========================================
# Sidebar
# ==========================================

search, trend, category, refresh = sidebar_filters()

if refresh:
    st.rerun()


# ==========================================
# Apply Filters
# ==========================================

filtered_df = df.copy()

if search:
    filtered_df = filtered_df[
        filtered_df["name"].str.contains(
            search,
            case=False
        )
    ]

if trend != "All":
    filtered_df = filtered_df[
        filtered_df["price_trend"] == trend
    ]

if category != "All":
    filtered_df = filtered_df[
        filtered_df["market_cap_category"] == category
    ]


# ==========================================
# Metrics
# ==========================================

show_metrics(filtered_df)


# ==========================================
# Charts
# ==========================================

left, right = st.columns(2)

with left:

    st.plotly_chart(
        market_cap_chart(filtered_df),
        width="stretch",
        key="market_cap_chart"
    )

with right:

    st.plotly_chart(
        trend_chart(filtered_df),
        width="stretch",
        key="trend_chart"
    )

st.plotly_chart(
    category_chart(filtered_df),
    width="stretch",
    key="category_chart"
)

st.divider()


# ==========================================
# Coin Details
# ==========================================

show_details(filtered_df)


# ==========================================
# Coin Table
# ==========================================

show_table(filtered_df)