from app.extract.pipeline import run_extraction_pipeline
from app.transform.cleaner import clean_dataframe

df = run_extraction_pipeline()

clean_df = clean_dataframe(df)

print(clean_df.info())

print()

print(clean_df.head())