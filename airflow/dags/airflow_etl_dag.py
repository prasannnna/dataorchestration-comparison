import sys
sys.path.append("/opt/airflow")

import pandas as pd
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from shared.etl_logic import extract_data, transform_data, load_data

INPUT_PATH = "/opt/airflow/data/input/user_events.csv"
OUTPUT_PATH = "/opt/airflow/data/output/airflow"

default_args = {
    "retries": 2,
    "retry_delay": timedelta(seconds=10),
}

def extract_task(ti):
    df = extract_data(INPUT_PATH)
    ti.xcom_push(key="df", value=df.to_json())

def transform_task(ti):
    df = pd.read_json(ti.xcom_pull(key="df"))
    df = transform_data(df, ["USA", "IND"], fail_randomly=True)
    ti.xcom_push(key="df", value=df.to_json())

def load_task(ti):
    df = pd.read_json(ti.xcom_pull(key="df"))
    load_data(df, OUTPUT_PATH)

with DAG(
    dag_id="airflow_user_etl",
    start_date=datetime(2026, 1, 1),
    schedule_interval=None,
    catchup=True,
    default_args=default_args,
) as dag:

    extract = PythonOperator(task_id="extract", python_callable=extract_task)
    transform = PythonOperator(task_id="transform", python_callable=transform_task)
    load = PythonOperator(task_id="load", python_callable=load_task)

    extract >> transform >> load
