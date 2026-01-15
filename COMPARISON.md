# Comparative Analysis of Data Orchestration Frameworks

## Apache Airflow vs Prefect vs Dagster

---

## 1. Project Overview

This project presents a **hands-on, implementation-based comparison** of three modern data orchestration frameworks:

* **Apache Airflow**
* **Prefect**
* **Dagster**

The comparison is performed by implementing the **exact same ETL pipeline** in all three frameworks, using a shared business logic layer and a synthetic user activity dataset (`user_events.csv`).

The goal is to evaluate the frameworks based on:

* Developer experience
* Core abstractions
* Retry and backfill mechanisms
* UI and observability
* Setup complexity
* Output parity

All pipelines reuse **identical transformation logic** to ensure a fair, apples-to-apples comparison.

---

## 2. Input Dataset

### Synthetic Dataset Description

* **File name:** `user_events.csv`
* **Location:** `data/input/user_events.csv`
* **Type:** Synthetic user activity data

**Fields:**

* `user_id`
* `event_type`
* `timestamp`
* `country`

This dataset is included in the repository and is used unchanged across all three orchestration frameworks.

---

## 3. Shared ETL Pipeline Logic

The ETL logic is implemented once in a shared Python module (`shared/etl_logic.py`) and reused by Airflow, Prefect, and Dagster **without modification**.

### Extract

* Reads the synthetic user events CSV file
* Input path is parameterized in all three pipelines

### Transform

* Filters events based on a configurable list of allowed countries
* Converts timestamps to datetime format
* Calculates session duration per user using first and last event timestamps
* Aggregates total number of events per user per day
* Introduces a controlled intermittent failure to validate retry behavior

### Load

* Writes the transformed data to Parquet format
* Output path is parameterized
* Output data is partitioned by event date

---

## 4. Orchestrator Implementations

### Apache Airflow

* Pipeline implemented as a **DAG**
* Tasks defined using `PythonOperator`
* Retries configured via DAG default arguments
* Backfills executed using Airflow CLI
* Runs inside Docker with SQLite metadata database

### Prefect

* Pipeline implemented as a **Flow**
* Tasks defined using the `@task` decorator
* Retry behavior configured directly at task level
* Parameterized runs used for historical execution
* Executed locally and via Docker

### Dagster

* Pipeline implemented as a **Job**
* Steps defined using `@op`
* Retry policy attached explicitly to the transform operation
* Historical runs executed by re-running jobs with parameters
* Executed locally and via Docker

---

## 5. Developer Experience

### Apache Airflow

**Pros**

* Industry-standard orchestration framework
* Strong scheduling and native backfill support
* Rich ecosystem of integrations

**Cons**

* More boilerplate code
* Slower development feedback loop
* Debugging often requires UI navigation

### Prefect

**Pros**

* Clean, Pythonic syntax
* Minimal boilerplate
* Excellent local development experience
* Simple and expressive retry configuration

**Cons**

* Smaller ecosystem compared to Airflow
* Some advanced features require Prefect Cloud

### Dagster

**Pros**

* Strong emphasis on data correctness and observability
* Explicit inputs and outputs improve clarity
* Well-suited for data-platform-oriented teams

**Cons**

* Steeper learning curve
* More concepts to understand initially

---

## 6. Core Concepts Comparison

| Framework | Core Abstractions   |
| --------- | ------------------- |
| Airflow   | DAG, Operator, Task |
| Prefect   | Flow, Task          |
| Dagster   | Job, Op             |

* **Airflow** focuses on workflow scheduling
* **Prefect** focuses on task execution and resiliency
* **Dagster** focuses on data dependencies and correctness

---

## 7. Retry Implementation

| Framework | Retry Mechanism                            |
| --------- | ------------------------------------------ |
| Airflow   | `retries`, `retry_delay` in DAG / operator |
| Prefect   | `@task(retries, retry_delay_seconds)`      |
| Dagster   | `RetryPolicy(max_retries, delay)`          |

All three pipelines successfully demonstrate retry behavior on the transformation step.

---

## 8. Backfill & Historical Runs

| Framework | Backfill Approach                    |
| --------- | ------------------------------------ |
| Airflow   | Native CLI backfill support          |
| Prefect   | Manual parameterized historical runs |
| Dagster   | Job re-execution with parameters     |

Airflow provides the most mature backfill experience out of the box.

---

## 9. UI & Observability

* **Airflow UI:** DAG graphs, task logs, historical runs, backfill controls
* **Prefect:** Clean terminal logs, optional UI when using server/cloud
* **Dagster:** Strong execution lineage and dependency visualization

---

## 10. Setup & Configuration Complexity

| Framework | Setup Complexity |
| --------- | ---------------- |
| Airflow   | High             |
| Prefect   | Low              |
| Dagster   | Medium           |

Airflow requires the most setup but provides the most operational features.

---

## 11. Output Parity Verification

All three pipelines were executed using:

* The same synthetic input dataset (`user_events.csv`)
* Identical transformation logic
* Identical parameters

The resulting Parquet outputs were verified to have:

* Identical schema
* Identical row counts
* Identical values
* Identical partitioning strategy

This confirms **true output parity** across all three implementations.

---

## 12. Summary Comparison Table

| Criteria            | Airflow | Prefect | Dagster |
| ------------------- | ------- | ------- | ------- |
| Ease of Development | Low     | High    | Medium  |
| Retry Configuration | Medium  | High    | High    |
| Backfill Support    | High    | Medium  | Medium  |
| UI & Observability  | High    | Medium  | High    |
| Setup Complexity    | High    | Low     | Medium  |

---

## 13. Final Recommendation

* **Apache Airflow** is ideal for scheduling-heavy, production-grade workflows
* **Prefect** is best for fast development and resilient pipelines
* **Dagster** is well-suited for data platforms requiring strong correctness guarantees

For most modern data teams, **Prefect offers the best balance between simplicity and power**, while Airflow remains the industry standard for complex scheduling use cases.

---

## 14. Conclusion

This project demonstrates that **Apache Airflow, Prefect, and Dagster** can all successfully orchestrate the same ETL pipeline, while differing significantly in design philosophy, usability, and operational complexity.

The **shared-logic approach** ensures a fair and meaningful comparison.
