from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from kubernetes.client.models import V1VolumeMount as VolumeMount
from kubernetes.client.models import V1Volume as Volume
from airflow.kubernetes.secret import Secret
from airflow import DAG
from airflow.utils.dates import days_ago

args = {
    "project_id": "airflow-pipeline-0327115148",
}

dag = DAG(
    "airflow-pipeline-0327115148",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.15.0.dev0 pipeline editor using `airflow-pipeline.pipeline`.
    """,
    is_paused_upon_creation=False,
    catchup=False,
)


# Operator source: examples/pipelines/setup_validation/python_notebook.ipynb

op_a65a7ef9_6ba1_492c_85fa_91e7f49c619c = KubernetesPodOperator(
    name="python_notebook",
    namespace="airflow",
    image="amancevice/pandas@sha256:f74bef70689b19d3cd610ef67227fce1c9a6ed8fa950ac2aff39ce72310d5520",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/main/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/main/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/main/etc/generic/requirements-elyra.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/main/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'airflow-pipeline' --cos-endpoint http://10.240.5.123:9099 --cos-bucket kube-secret-test --cos-directory 'airflow-pipeline-0327115148' --cos-dependencies-archive 'python_notebook-a65a7ef9-6ba1-492c-85fa-91e7f49c619c.tar.gz' --file 'examples/pipelines/setup_validation/python_notebook.ipynb' "
    ],
    task_id="python_notebook",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "airflow-pipeline-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[
        Secret("env", "AWS_ACCESS_KEY_ID", "minio-secret", "AWS_ACCESS_KEY_ID"),
        Secret("env", "AWS_SECRET_ACCESS_KEY", "minio-secret", "AWS_SECRET_ACCESS_KEY"),
    ],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file=None,
    dag=dag,
)


# Operator source: examples/pipelines/setup_validation/python_script.py

op_7699ca44_86ae_4f4f_a31b_973bfa3cf152 = KubernetesPodOperator(
    name="python_script",
    namespace="airflow",
    image="amancevice/pandas@sha256:f74bef70689b19d3cd610ef67227fce1c9a6ed8fa950ac2aff39ce72310d5520",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/main/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/main/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/main/etc/generic/requirements-elyra.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/main/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'airflow-pipeline' --cos-endpoint http://10.240.5.123:9099 --cos-bucket kube-secret-test --cos-directory 'airflow-pipeline-0327115148' --cos-dependencies-archive 'python_script-7699ca44-86ae-4f4f-a31b-973bfa3cf152.tar.gz' --file 'examples/pipelines/setup_validation/python_script.py' "
    ],
    task_id="python_script",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "airflow-pipeline-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[
        Secret("env", "AWS_ACCESS_KEY_ID", "minio-secret", "AWS_ACCESS_KEY_ID"),
        Secret("env", "AWS_SECRET_ACCESS_KEY", "minio-secret", "AWS_SECRET_ACCESS_KEY"),
    ],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file=None,
    dag=dag,
)

op_7699ca44_86ae_4f4f_a31b_973bfa3cf152 << op_a65a7ef9_6ba1_492c_85fa_91e7f49c619c
