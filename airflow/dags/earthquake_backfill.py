from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models.param import Param
import httpx
def query_usgs(**context):
 p=context['params']; response=httpx.get(context['var']['value'].get('usgs_query_url','https://earthquake.usgs.gov/fdsnws/event/1/query'),params={'format':'geojson','starttime':p['start_date'],'endtime':p['end_date'],'minmagnitude':p['minimum_magnitude'],'maxmagnitude':p['maximum_magnitude'],'limit':p['limit']},timeout=30);response.raise_for_status();context['ti'].xcom_push(key='features',value=response.json().get('features',[]))
with DAG('earthquake_backfill',start_date=datetime(2025,1,1),schedule=None,catchup=False,params={'start_date':Param('2025-01-01',type='string'),'end_date':Param('2025-01-02',type='string'),'minimum_magnitude':Param(4,type='number'),'maximum_magnitude':Param(10,type='number'),'limit':Param(500,type='integer')},tags=['backfill','earthquake']) as dag:
 PythonOperator(task_id='query_bounded_usgs_history',python_callable=query_usgs)
