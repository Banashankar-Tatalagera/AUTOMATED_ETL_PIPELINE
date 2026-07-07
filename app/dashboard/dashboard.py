import streamlit as st
import pandas as pd

from api_client import get_all_coins

from sidebar import sidebar_filters
from metrics import show_metrics
from charts import (
    market_cap_chart,
    trend_chart,
    category_chart,
)
from details import show_details
from table import show_table


# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="Crypto ETL Dashboard",
    page_icon="📈",
    layout="wide",
)

st.title("📈 Crypto ETL Dashboard")


# ==========================================
# Load Data
# ==========================================

@st.cache_data(ttl=60)
def load_data():
    coins = get_all_coins()
    return pd.DataFrame(coins)


try:
    df = load_data()

except Exception as e:
    st.error(f"Unable to fetch data from the API.\n\n{e}")
    st.stop()


if df.empty:
    st.warning("No cryptocurrency data found.")
    st.stop()


# ==========================================
# Sidebar
# ==========================================

search, trend, category, refresh = sidebar_filters()

if refresh:
    st.cache_data.clear()
    st.rerun()


# ==========================================
# Apply Filters
# ==========================================

filtered_df = df.copy()

if search:
    filtered_df = filtered_df[
        filtered_df["name"].str.contains(
            search,
            case=False,
            na=False
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


if filtered_df.empty:
    st.warning("No coins match the selected filters.")
    st.stop()


# ==========================================
# Metrics
# ==========================================

show_metrics(filtered_df)

st.divider()


# ==========================================
# Charts
# ==========================================

left, right = st.columns(2)

with left:

    st.plotly_chart(
        market_cap_chart(filtered_df),
        use_container_width=True,
        key="market_cap_chart",
    )

with right:

    st.plotly_chart(
        trend_chart(filtered_df),
        use_container_width=True,
        key="trend_chart",
    )

st.plotly_chart(
    category_chart(filtered_df),
    use_container_width=True,
    key="category_chart",
)

st.divider()


# ==========================================
# Coin Details
# ==========================================

show_details(filtered_df)

st.divider()


# ==========================================
# Coin Table
# ==========================================

show_table(filtered_df)


# ==========================================
# Footer
# ==========================================

st.caption(
    "Crypto ETL Dashboard • Built with FastAPI, PostgreSQL, Streamlit, Plotly & Docker"
)