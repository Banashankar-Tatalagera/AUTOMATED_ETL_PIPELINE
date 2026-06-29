from app.extract.pipeline import run_extraction_pipeline
from app.transform.pipeline import run_transformation_pipeline

raw_df = run_extraction_pipeline()

final_df = run_transformation_pipeline(raw_df)

print(final_df.head())

print()

print(final_df.info())

print()

print(final_df.shape)