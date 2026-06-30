from app.extract.client import fetch_data
from app.extract.validator import validate_response
from app.extract.parser import parse_to_dataframe

response = fetch_data()

data = validate_response(response)

df = parse_to_dataframe(data)

print(type(df))
print(df.head())

print(df.info())