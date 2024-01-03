from airflow import DAG
from airflow.operators.bash import BashOperator

# other packages
from datetime import timedelta
from datetime import datetime
from airflow.utils.dates import days_ago



default_args = {
    'owner': 'santiagoMeneses',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(seconds=5)
}


dag = DAG(  dag_id='price_alert',
            description='Get last prices',
            default_args=default_args,
            start_date=datetime(2023, 3, 25, 00, 00, 00),
            schedule_interval='/15 * * * *',
            catchup=False,
            concurrency=1,
            dagrun_timeout=timedelta(minutes=5),
            tags=['pruebas'])

task_1 = BashOperator(
    task_id='get_last_prices',
    bash_command='/data/anaconda3/envs/binance/bin/python /data/patrones/test/main.py',
    dag=dag,
)

