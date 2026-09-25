from datetime import datetime
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
with DAG('earthquake_quality',start_date=datetime(2025,1,1),schedule='@daily',catchup=False,tags=['quality','earthquake']) as dag:
 PostgresOperator(task_id='validate_raw_events',postgres_conn_id='earthquake_postgres',sql="""select case when exists (select 1 from raw.earthquake_events where event_time is null or latitude not between -90 and 90 or longitude not between -180 and 180 or magnitude not between -2 and 10 or (updated_time is not null and updated_time < event_time)) then 1/0 else 1 end;""")
