from app.extract.client import fetch_data

response = fetch_data()

print("Type :", type(response))

print("Status Code :", response.status_code)

print("Reason :", response.reason)

print("Content Type :", response.headers["Content-Type"])