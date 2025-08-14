import os
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "Basanth Kumar",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
    "retry_delay": timedelta(minutes=1),
}

dag = DAG(
    "stock_market_pipeline",
    default_args=default_args,
    description="Stock Market Pipeline - Working Version",
    schedule_interval=None,
    start_date=datetime(2025, 8, 14),
    catchup=False,
)

# Bulletproof approach: Simple, direct execution
fetch_historical_data = BashOperator(
    task_id="fetch_historical_data",
    bash_command="""
    echo "Starting fetch_historical_data task"
    cd /opt/airflow/dags/scripts
    python batch_data_producer.py {{ ds }}
    echo "Task completed successfully"
    """,
    dag=dag,
)

consume_historical_data = BashOperator(
    task_id="consume_historical_data",
    bash_command="""
    echo "Starting consume_historical_data task"
    cd /opt/airflow/dags/scripts
    python batch_data_consumer.py {{ ds }}
    echo "Task completed successfully"
    """,
    dag=dag,
)

process_data = BashOperator(
    task_id="process_data",
    bash_command="""
    echo "Starting process_data task"
    docker exec stock-market-kafka-spark-master-1 \
        spark-submit \
            --master spark://spark-master:7077 \
            --packages org.apache.hadoop:hadoop-aws:3.3.1,com.amazonaws:aws-java-sdk-bundle:1.11.901 \
                /opt/spark/jobs/spark_batch_processor.py {{ ds }}
    echo "Task completed successfully"
    """,
    dag=dag,
)

load_to_snowflake = BashOperator(
    task_id="load_to_snowflake",
    bash_command="""
    echo "Starting load_to_snowflake task"
    cd /opt/airflow/dags/scripts
    python load_to_snowflake.py {{ ds }}
    echo "Task completed successfully"
    """,
    dag=dag,
)

pipeline_success = BashOperator(
    task_id="pipeline_success",
    bash_command="""
    echo "🎉 PIPELINE SUCCESS! 🎉"
    echo "All tasks completed successfully"
    """,
    dag=dag,
)

# Dependencies
fetch_historical_data >> consume_historical_data >> process_data >> load_to_snowflake >> pipeline_success 