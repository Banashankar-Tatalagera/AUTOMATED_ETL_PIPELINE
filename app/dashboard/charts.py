import plotly.express as px


def market_cap_chart(df):

    top10 = (
        df.sort_values(
            "market_cap",
            ascending=False
        )
        .head(10)
    )

    fig = px.bar(
        top10,
        x="market_cap",
        y="name",
        orientation="h",
        title="Top 10 Coins by Market Cap"
    )

    fig.update_layout(
        yaxis=dict(autorange="reversed")
    )

    return fig


def trend_chart(df):

    counts = (
        df["price_trend"]
        .value_counts()
        .reset_index()
    )

    counts.columns = [
        "Trend",
        "Count"
    ]

    fig = px.pie(
        counts,
        names="Trend",
        values="Count",
        title="Bullish vs Bearish"
    )

    return fig


def category_chart(df):

    counts = (
        df["market_cap_category"]
        .value_counts()
        .reset_index()
    )

    counts.columns = [
        "Category",
        "Count"
    ]

    fig = px.pie(
        counts,
        names="Category",
        values="Count",
        hole=0.45,
        title="Market Cap Distribution"
    )

    return fig