import os
import pandas as pd
from llama_index.core.query_engine import PandasQueryEngine
from prompts import new_prompt, instruction_str

job_listings_path = os.path.join("data", "job_listings.csv")
job_listings_df = pd.read_csv(job_listings_path)

job_listings_engine = PandasQueryEngine(
    df=job_listings_df, verbose=True, instruction_str=instruction_str
)
job_listings_engine.update_prompts({"pandas_prompt": new_prompt})