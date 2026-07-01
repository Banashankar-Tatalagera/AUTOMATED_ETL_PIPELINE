from app.extract.client import fetch_data

try:
    response = fetch_data()

    print(f"Status Code : {response.status_code}")
    print(f"Reason      : {response.reason}")
    print(f"Content-Type: {response.headers['Content-Type']}")

except Exception as e:
    print(f"Error: {e}")