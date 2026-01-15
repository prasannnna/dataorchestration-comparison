import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from prefect import flow, task
from shared.etl_logic import extract_data, transform_data, load_data


@task(retries=2, retry_delay_seconds=10)
def extract(input_path):
    return extract_data(input_path)

@task(retries=2, retry_delay_seconds=10)
def transform(df):
    return transform_data(df, ["USA", "IND"], fail_randomly=True)

@task
def load(df, output_path):
    load_data(df, output_path)

@flow
def prefect_etl(input_path, output_path):
    df = extract(input_path)
    df = transform(df)
    load(df, output_path)

if __name__ == "__main__":
    prefect_etl(
        "data/input/user_events.csv",
        "data/output/prefect"
    )
