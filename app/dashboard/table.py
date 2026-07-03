import streamlit as st


def show_table(df):

    st.subheader("📋 Coin Data")

    st.dataframe(
        df,
        width="stretch",
        hide_index=True
    )

    st.download_button(
        "📥 Download CSV",
        data=df.to_csv(index=False),
        file_name="crypto_data.csv",
        mime="text/csv"
    )