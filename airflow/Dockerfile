FROM apache/airflow:2.10.4-python3.12

USER root
# any OS-level deps you need, e.g. for postgres client libs
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

USER airflow

# Airflow's own deps (confluent-kafka, httpx are fine here — no conflicts)
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt \
    --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.10.4/constraints-3.12.txt"

# dbt lives in its own isolated venv — avoids all dependency conflicts
RUN python -m venv /home/airflow/dbt_venv && \
    /home/airflow/dbt_venv/bin/pip install --no-cache-dir dbt-postgres==1.8.2

ENV PATH="/home/airflow/dbt_venv/bin:$PATH"