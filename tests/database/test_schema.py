from app.database.connection import Base, engine

import app.database.schema

Base.metadata.create_all(bind=engine)

print("Tables created successfully.")