from app.extract.pipeline import run_extraction_pipeline
from app.transform.cleaner import clean_dataframe
from app.transform.engineer import engineer_features

df = run_extraction_pipeline()

clean_df = clean_dataframe(df)

engineered_df = engineer_features(clean_df)

print(engineered_df.head())

print()

print(engineered_df.columns)