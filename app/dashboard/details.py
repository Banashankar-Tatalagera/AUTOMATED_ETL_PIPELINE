import streamlit as st


def show_details(df):

    st.subheader("🪙 Coin Details")

    selected = st.selectbox(
        "Choose Coin",
        df["name"]
    )

    coin = df[
        df["name"] == selected
    ].iloc[0]

    c1, c2 = st.columns(2)

    with c1:

        st.metric(
            "Current Price",
            f"${coin['current_price']:,.2f}"
        )

        st.metric(
            "Market Cap Rank",
            int(coin["market_cap_rank"])
        )

    with c2:

        st.metric(
            "Market Cap",
            f"${coin['market_cap']:,.0f}"
        )

        st.metric(
            "24 Hour Change",
            f"{coin['price_change_percentage_24h']:.2f}%"
        )

    st.divider()