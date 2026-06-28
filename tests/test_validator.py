from app.extract.client import fetch_data
from app.extract.validator import validate_response

response = fetch_data()

data = validate_response(response)

print(type(data))
print(len(data))
print(data[0])