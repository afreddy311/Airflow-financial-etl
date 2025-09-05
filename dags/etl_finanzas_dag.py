from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data

#definicion de funciones intermedias
def run_extract(**kwargs):
    df = extract_data('data/transacciones_financieras.csv')
    kwargs['ti'].xcom_push(key='raw_data', value=df.to_json())

def run_transform(**kwargs):
    import pandas as pd
    raw_json = kwargs['ti'].xcom_pull(key='raw_data', task_ids='extract')
    df_raw = pd.read_json(raw_json)
    df_transformed = transform_data(df_raw)
    kwargs['ti'].xcom_push(key='transformed_data', value=df_transformed.to_json())

def run_load(**kwargs):
    import pandas as pd
    transformed_json = kwargs['ti'].xcom_pull(key='transformed_data', task_ids='transform')
    df_transformed = pd.read_json(transformed_json)
    load_data(df_transformed, 'data/resumen_gasto_mensual.csv')

# Argumentos por defecto del DAG
default_args = {'owner': 'Freddy', 'start_date': datetime(2025, 9,4 ),'retries': 1}

# Definición del DAG
with DAG('etl_finanzas_dag', default_args=default_args, schedule_interval='@daily', catchup=False) as dag:

    extract = PythonOperator(
        task_id='extract',
        python_callable=run_extract,
        provide_context=True
    )

    transform = PythonOperator(
        task_id='transform',
        python_callable=run_transform,
        provide_context=True
    )

    load = PythonOperator(
        task_id='load',
        python_callable=run_load,
        provide_context=True
    )

    # Definición del flujo de tareas
    extract >> transform >> load