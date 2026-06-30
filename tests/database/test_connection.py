from app.database.connection import get_session

session = get_session()

print(type(session))

session.close()

print("Database session closed successfully.")
