from app.extract.pipeline import run_extraction_pipeline
from app.transform.pipeline import run_transformation_pipeline
from app.load.loader import load_dataframe

raw_df = run_extraction_pipeline()

final_df = run_transformation_pipeline(raw_df)

load_dataframe(final_df)