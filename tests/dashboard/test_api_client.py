from app.dashboard.api_client import get_top10

coins = get_top10()

print(type(coins))

print(len(coins))

print(coins[0]["name"])
