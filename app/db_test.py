from sqlalchemy import create_engine
from config import DATABASE_URL

try:
    engine = create_engine(DATABASE_URL)

    with engine.connect() as conn:
        print("Connected Successfully!")

except Exception as e:
    print(e)

    