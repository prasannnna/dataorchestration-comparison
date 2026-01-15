# Apache Airflow Implementation

This directory contains the Apache Airflow implementation of the ETL pipeline.

---

##  Tools & Technologies
- Apache Airflow
- Python
- Docker & Docker Compose
- Pandas
- PyArrow

---

##  Structure
```
airflow/
├── dags/
│ └── airflow_etl_dag.py
├── docker-compose.yml
└── README.md

```

---

## How to Run Airflow

### Step 1: Start Airflow

```bash
docker-compose up -d
```
### Step 2: Access Airflow UI
- Open in browser:

```
http://localhost:8080
```
### Login credentials (if applicable):
```
Username: admin

Password: admin
```
- Trigger DAG Run
- From the Airflow UI:

- Enable the DAG **airflow_user_etl**

- Trigger a manual run

### Backfill Execution
### To demonstrate historical runs:
```
docker exec -it airflow airflow dags backfill -s 2026-01-02 -e 2026-01-03 user_etl_pipeline
```
### Retry Configuration
### Retries are configured at the DAG level:

- Retries: 2

- Retry delay: 10 seconds

- Retries are triggered automatically if the transform task fails.


### Included Screenshots

1. **dag_success.png**
   - Shows the DAG `user_etl_pipeline` visible in the Airflow Web UI
   - Confirms successful DAG discovery and loading
   - Access at **screenshots/airflow/dag_success.png**

2. **backfill_runs.png**
   - Shows a successful DAG run / backfill execution
   - Demonstrates historical execution capability (backfill)
   - Access at **screenshots/airflow/backfill_runs.png**

These screenshots collectively demonstrate:
- DAG authoring
- Dependency management
- Successful execution
- Backfill support in Airflow


### Stop Services
```
docker-compose down
```
