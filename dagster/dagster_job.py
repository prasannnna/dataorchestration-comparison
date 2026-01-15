from dagster import job, op, RetryPolicy
from shared.etl_logic import extract_data, transform_data, load_data

@op
def extract():
    return extract_data("data/input/user_events.csv")

@op(
    retry_policy=RetryPolicy(max_retries=2, delay=10)
)
def transform(df):
    return transform_data(df, ["USA", "IND"], fail_randomly=True)

@op
def load(df):
    load_data(df, "data/output/dagster")

@job
def dagster_etl():
    load(transform(extract()))
