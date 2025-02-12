import datetime as dt
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

path = '/opt/airflow/dags/'

default_args = {
    'owner': 'Danes',
    'start_date': dt.datetime(2025, 1, 16),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=600),
}


with DAG('data_pipeline_m3_daniswara',
        default_args=default_args,
        schedule_interval='*/20 * * * *',
        catchup=False,
        ) as dag:

    extract = BashOperator(task_id='extract',
                            bash_command=f'sudo -u airflow python {path}/data_pipeline_extract.py')
    transform = BashOperator(task_id='transform',
                            bash_command=f'sudo -u airflow python {path}/data_pipeline_transform.py')
    load = BashOperator(task_id='load',
                            bash_command=f'sudo -u airflow python {path}/data_pipeline_load.py')

extract >> transform >> load

