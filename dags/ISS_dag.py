from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from issloc import fetch_iss_location

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 7, 8),
    'retries': 1,
    'retry_delay': timedelta(seconds=30),
}

dag = DAG(
    'iss_location',
    default_args=default_args,
    description='A simple DAG to get ISS location',
    schedule_interval=timedelta(seconds=30),
)

fetch_iss_task = PythonOperator(
    task_id='fetch_iss_location',
    python_callable=fetch_iss_location,
    provide_context=True,
    dag=dag,
)

