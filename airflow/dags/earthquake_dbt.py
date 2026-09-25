from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

DBT_BIN = "/home/airflow/dbt_venv/bin/dbt"
DBT_PROJECT_DIR = "/opt/airflow/dbt/earthquake_analytics"
DBT_PROFILES_DIR = "/opt/airflow/dbt"

with DAG(
    'earthquake_dbt',
    start_date=datetime(2025, 1, 1),
    schedule='@hourly',
    catchup=False,
    tags=['dbt', 'earthquake'],
) as dag:

    deps = BashOperator(
        task_id='dbt_deps',
        bash_command=f'cd {DBT_PROJECT_DIR} && {DBT_BIN} deps --profiles-dir {DBT_PROFILES_DIR}',
    )

    run = BashOperator(
        task_id='dbt_run',
        bash_command=f'cd {DBT_PROJECT_DIR} && {DBT_BIN} run --profiles-dir {DBT_PROFILES_DIR}',
    )

    test = BashOperator(
        task_id='dbt_test',
        bash_command=f'cd {DBT_PROJECT_DIR} && {DBT_BIN} test --profiles-dir {DBT_PROFILES_DIR}',
    )

    deps >> run >> test