from airflow.providers.docker.operators.docker import DockerOperator
from airflow import DAG
from airflow.utils.dates import days_ago

args = {
    "project_id": "test-demo-0425171816",
}

dag = DAG(
    "test-demo-0425171816",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.15.0.dev0 pipeline editor using `untitled.pipeline`.
    """,
    is_paused_upon_creation=False,
    catchup=False,
)


# Operator source: examples/pipelines/setup_validation/python_notebook.ipynb

op_03bfb9eb_5953_4bd3_88ed_b8c0a69c15bd = DockerOperator(
    name="python_notebook",
    image="amancevice/pandas@sha256:f74bef70689b19d3cd610ef67227fce1c9a6ed8fa950ac2aff39ce72310d5520",
    docker_url="tcp://dind:2375",
    command=[
        "sh",
        "-c",
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/main/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/main/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/main/etc/generic/requirements-elyra.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/main/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'test-demo' --cos-endpoint http://10.240.5.123:9099 --cos-bucket test-demo --cos-directory 'test-demo-0425171816' --cos-dependencies-archive 'python_notebook-03bfb9eb-5953-4bd3-88ed-b8c0a69c15bd.tar.gz' --file 'examples/pipelines/setup_validation/python_notebook.ipynb' ",
    ],
    task_id="python_notebook",
    environment={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "X64L1MDB4CTM1TT4TZZK",
        "AWS_SECRET_ACCESS_KEY": "qQEt+7C+zYdjYG7+ApNSQ8eRCnw4ME2M4qu9ngfq",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "test-demo-{{ ts_nodash }}",
    },
    mount_tmp_dir=False,
    network_mode="bridge",
    dag=dag,
)


# Operator source: examples/pipelines/setup_validation/python_script.py

op_7bb27a36_deab_4f55_88dd_667d10117a0b = DockerOperator(
    name="python_script",
    image="amancevice/pandas@sha256:f74bef70689b19d3cd610ef67227fce1c9a6ed8fa950ac2aff39ce72310d5520",
    docker_url="tcp://dind:2375",
    command=[
        "sh",
        "-c",
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/main/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/main/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/main/etc/generic/requirements-elyra.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/main/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'test-demo' --cos-endpoint http://10.240.5.123:9099 --cos-bucket test-demo --cos-directory 'test-demo-0425171816' --cos-dependencies-archive 'python_script-7bb27a36-deab-4f55-88dd-667d10117a0b.tar.gz' --file 'examples/pipelines/setup_validation/python_script.py' ",
    ],
    task_id="python_script",
    environment={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "X64L1MDB4CTM1TT4TZZK",
        "AWS_SECRET_ACCESS_KEY": "qQEt+7C+zYdjYG7+ApNSQ8eRCnw4ME2M4qu9ngfq",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "test-demo-{{ ts_nodash }}",
    },
    mount_tmp_dir=False,
    network_mode="bridge",
    dag=dag,
)

op_7bb27a36_deab_4f55_88dd_667d10117a0b << op_03bfb9eb_5953_4bd3_88ed_b8c0a69c15bd
