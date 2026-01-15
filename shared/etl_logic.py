import pandas as pd
import os
import random
import time

def extract_data(input_path):
    return pd.read_csv(input_path)

def transform_data(df, allowed_countries, fail_randomly=False):
    # Failure simulation for retries
    if fail_randomly and random.random() < 0.3:
        raise Exception("Simulated intermittent failure")

    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df[df["country"].isin(allowed_countries)]

    session_df = df.groupby("user_id").agg(
        session_start=("timestamp", "min"),
        session_end=("timestamp", "max")
    ).reset_index()

    session_df["session_duration_sec"] = (
        session_df["session_end"] - session_df["session_start"]
    ).dt.total_seconds()

    df["event_date"] = df["timestamp"].dt.date

    agg_df = df.groupby(
        ["user_id", "event_date"]
    ).size().reset_index(name="event_count")

    final_df = agg_df.merge(session_df, on="user_id", how="left")
    return final_df

def load_data(df, output_path):
    os.makedirs(output_path, exist_ok=True)
    df.to_parquet(
        os.path.join(output_path, "result.parquet"),
        partition_cols=["event_date"]
    )
