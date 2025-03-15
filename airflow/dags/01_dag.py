from airflow import DAG
from airflow.operators.python import PythonOperator 

from datetime import timedelta, datetime
import pandas as pd
from faker import Faker


import logging

logger = logging.getLogger(__name__)


def create_dataframe():
    fake = Faker()
    data = {
        "Name": [fake.name() for _ in range(5)],
        "Address": [fake.address() for _ in range(5)],
        "Email": [fake.email() for _ in range(5)]
    }

    df_fake = pd.DataFrame(data)
    logger.info(df_fake)
    


with DAG(
    dag_id="01_pattern_name_dag",
    default_args={'retries':1},
    start_date=datetime.now(),
    tags=["example", "learning"],
    schedule="@daily",
    catchup=False,
    dagrun_timeout=timedelta(minutes=20)
):
    
    t1 = PythonOperator(
        task_id="python_task",
        python_callable=create_dataframe,
        # op_kwargs: Optional[Dict] = None,
        # op_args: Optional[List] = None,
        # templates_dict: Optional[Dict] = None
        # templates_exts: Optional[List] = None
    )

    t1
