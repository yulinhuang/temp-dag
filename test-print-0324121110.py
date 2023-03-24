from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from kubernetes.client.models import V1VolumeMount as VolumeMount
from kubernetes.client.models import V1Volume as Volume
from airflow.kubernetes.secret import Secret
from airflow import DAG
from airflow.utils.dates import days_ago

args = {
    "project_id": "test-print-0324121110",
}

dag = DAG(
    "test-print-0324121110",
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

op_4f5820cc_9415_4668_90f2_09deb7fbe5bd = KubernetesPodOperator(
    name="python_notebook",
    namespace="airflow",
    image="continuumio/anaconda3@sha256:a2816acd3acda208d92e0bf6c11eb41fda9009ea20f24e123dbf84bb4bd4c4b8",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/main/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/main/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/main/etc/generic/requirements-elyra.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/main/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'test-print' --cos-endpoint http://10.240.5.123:9099 --cos-bucket test --cos-directory 'test-print-0324121110' --cos-dependencies-archive 'python_notebook-4f5820cc-9415-4668-90f2-09deb7fbe5bd.tar.gz' --file 'examples/pipelines/setup_validation/python_notebook.ipynb' "
    ],
    task_id="python_notebook",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "X64L1MDB4CTM1TT4TZZK",
        "AWS_SECRET_ACCESS_KEY": "qQEt+7C+zYdjYG7+ApNSQ8eRCnw4ME2M4qu9ngfq",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "test-print-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file=None,
    dag=dag,
)


# Operator source: examples/pipelines/setup_validation/python_script.py

op_0b0bf262_bc90_4ece_b41b_042f002aef64 = KubernetesPodOperator(
    name="python_script",
    namespace="airflow",
    image="continuumio/anaconda3@sha256:a2816acd3acda208d92e0bf6c11eb41fda9009ea20f24e123dbf84bb4bd4c4b8",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/main/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/main/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/main/etc/generic/requirements-elyra.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/main/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'test-print' --cos-endpoint http://10.240.5.123:9099 --cos-bucket test --cos-directory 'test-print-0324121110' --cos-dependencies-archive 'python_script-0b0bf262-bc90-4ece-b41b-042f002aef64.tar.gz' --file 'examples/pipelines/setup_validation/python_script.py' "
    ],
    task_id="python_script",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "X64L1MDB4CTM1TT4TZZK",
        "AWS_SECRET_ACCESS_KEY": "qQEt+7C+zYdjYG7+ApNSQ8eRCnw4ME2M4qu9ngfq",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "test-print-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file=None,
    dag=dag,
)

op_0b0bf262_bc90_4ece_b41b_042f002aef64 << op_4f5820cc_9415_4668_90f2_09deb7fbe5bd
