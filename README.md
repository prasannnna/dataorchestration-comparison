# Comparative Analysis of Data Orchestration Frameworks

This repository contains a hands-on comparison of three popular data orchestration frameworks:
- Apache Airflow
- Prefect
- Dagster

The same ETL pipeline is implemented using each framework to evaluate differences in developer experience, core concepts, orchestration features, and operational behavior.

---

##  Project Objective

The goal of this project is to:
- Implement an identical ETL pipeline in Airflow, Prefect, and Dagster
- Compare how each framework handles DAG authoring, retries, parameterization, and backfills
- Provide an evidence-based analysis to help choose the right orchestration tool for different scenarios

---

##  Repository Structure
```
data-orchestration-comparison/
│
├── airflow/
│ ├── dags/
│ ├── docker-compose.yml
│ └── README.md
│
├── prefect/
│ ├── prefect_flow.py
│ ├── docker-compose.yml
│ └── README.md
│
├── dagster/
│ ├── dagster_job.py
│ ├── docker-compose.yml
│ └── README.md
│
├── shared/
│ └── etl_logic.py
│
├── data/
│ ├── input/
│ │ └── user_events.csv
│ └── output/
│
├── screenshots/
│ ├── airflow/
│ ├── prefect/
│ └── dagster/
│
├── COMPARISON.md
└── README.md

```

---

##  Input Dataset: user_events.csv(synthetic_events.csv)

The input data used across all three orchestration frameworks is a synthetic dataset stored at:


```
data/input/user_events.csv
```

### Dataset Description

The dataset represents synthetic user activity events and contains the following columns:

| Column Name | Description |
|------------|------------|
| user_id | Unique identifier for each user |
| event_type | Type of user action (e.g., click, view, purchase) |
| timestamp | Timestamp of the event |
| country | Country where the event originated |

### Purpose

This dataset is used to:
- Simulate real-world user activity
- Ensure identical input across Airflow, Prefect, and Dagster
- Verify output parity across all pipeline implementations

The same dataset is consumed by all three orchestrators without modification.

## Shared ETL Logic

The core ETL logic is implemented once in `shared/etl_logic.py` and reused across all orchestrators to ensure:
- Identical transformations
- Output parity
- Fair comparison

ETL Steps:
1. Extract data from CSV
2. Transform:
   - Filter by country
   - Calculate session duration
   - Aggregate events per user per day
3. Load aggregated data into Parquet format

---

## How to Run

Each orchestrator has its own directory and README with detailed instructions.

Please refer to:
- `airflow/README.md`
- `prefect/README.md`
- `dagster/README.md`

---

## Comparison & Analysis

A detailed analysis comparing Airflow, Prefect, and Dagster is available in:

 `COMPARISON.md`

---

##  Evaluation Notes

- All pipelines are Dockerized
- Retry logic is implemented in the transform step
- Backfill capability is demonstrated and documented
- Outputs are identical for the same inputs

---

