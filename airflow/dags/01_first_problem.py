from airflow import DAG
from airflow.operators.python import PythonOperator

import logging
from typing import Optional, List

from datetime import timedelta, datetime

logger = logging.getLogger(__name__)


with DAG(
    dag_id='01_find_even_or_odd',
    default_args={'retries':1},
    description='A simple tutorial DAG',
    schedule_interval=timedelta(days=1),
    start_date=datetime.now(),
    catchup=False,
    tags=['example'],
) as dag:
    
    python_task = PythonOperator(
        task_id="python_task",
        python_callable=lambda number: logger.info('--> Odd') if number%2 == 0 else logger.info('---> even'),
        # op_kwargs: Optional[Dict] = None,
        op_args = [5],
        # templates_dict: Optional[Dict] = None
        # templates_exts: Optional[List] = None
    )

    python_task