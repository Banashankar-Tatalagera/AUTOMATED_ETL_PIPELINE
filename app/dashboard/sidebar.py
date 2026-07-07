import streamlit as st


def sidebar_filters():

    st.sidebar.header("Filters")

    search = st.sidebar.text_input(
        "Search Coin",
        placeholder="Bitcoin..."
    )

    trend = st.sidebar.selectbox(
        "Price Trend",
        [
            "All",
            "Bullish",
            "Bearish"
        ]
    )

    category = st.sidebar.selectbox(
        "Market Cap",
        [
            "All",
            "Large Cap",
            "Mid Cap",
            "Small Cap"
        ]
    )

    refresh = st.sidebar.button("🔄 Refresh Data")

    return search, trend, category, refresh