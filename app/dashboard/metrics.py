import streamlit as st


def show_metrics(df):

    total = len(df)

    bullish = len(
        df[df["price_trend"] == "Bullish"]
    )

    bearish = len(
        df[df["price_trend"] == "Bearish"]
    )

    large = len(
        df[df["market_cap_category"] == "Large Cap"]
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Total Coins", total)
    c2.metric("Bullish", bullish)
    c3.metric("Bearish", bearish)
    c4.metric("Large Cap", large)

    st.divider()