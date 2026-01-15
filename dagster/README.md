# Dagster Implementation

This directory contains the Dagster job-based implementation of the ETL pipeline.

---

##  Tools & Technologies
- Dagster
- Python
- Docker & Docker Compose
- Pandas
- PyArrow

---

##  Structure
```
dagster/
├── dagster_job.py
├── docker-compose.yml
└── README.md
```


---

##  How to Run Dagster Job

### Step 1: Start the Dagster container

```bash
docker-compose up
```
### The container:

- Installs Dagster and dependencies

- Executes the Dagster job once

- Exits after completion

### Retry Configuration
- Retries are configured at the op level using RetryPolicy.

- Retries are triggered only when an op fails.
In this execution, all ops completed successfully on the first attempt.

### Execution Evidence
- Dagster execution logs show:

- Job start

- Step-level execution (extract, transform, load)

- Successful job completion

### Logs are captured using:

```
docker logs dagster
```
### Screenshots Provided

### Included Screenshot

1. **job_success.png**
   - Shows successful execution of the Dagster job
   - Displays step-level execution for `extract`, `transform`, and `load`
   - Confirms completion of the Dagster pipeline
   - Access at **screenshots/dagster/job_success.png**

### Note on Retries

Retry behavior in Dagster is configured at the op level using `RetryPolicy`.
Retries are triggered only when an op fails.

In the provided execution, all ops completed successfully on the first attempt, so no retry was triggered.
The retry configuration is visible in the Dagster job definition code.


### Stop Services
```
docker-compose down
```
