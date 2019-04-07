## Install the followings:

```bash
sudo apt-get install libmysqlclient-dev
sudo apt-get install libssl-dev
sudo apt-get install libkrb5-dev
sudo apt-get install libsasl2-dev
sudo apt install python3-pip
sudo apt install virtualenv
```

## Install Airflow:

```bash
vim ~/.bashrc
export SLUGIFY_USES_TEXT_UNIDECO=yes
export AIRFLOW_HOME=~/airflow
export AIRFLOW_GPL_UNIDECODE=yes
export PATH=$PATH:~/.local/bin
export S3_BUCKET=<S3_BUCKET_FOR_CSV_FILES>
export AIRFLOW_CONN_S3_URI=s3://<AWS_ACCESS_KEY_ID>:<AWS_SECRET_ACCESS_KEY>@<AWS_SECRET_ACCESS_KEY>/*

pip3 install apache-airflow[celery,crypto,postgres,rabbitmq,redis]
pip3 install -r requirements.txt
```

## Initialize airflow db

```bash
airflow initdb
```

## Make dags folder

```bash
mkdir /home/ubuntu/airflow/dags
```

## Change airflow.cfg

```bash
* base_url --> 8083
* webserver_port --> 8083
* load_example --> False
* airflow resetdb
* executor = CeleryExecutorr
* sql_alchemy_conn = postgresql+psycopg2://<postgres_instance_private_IP>:5432/airflow
* broker_url = pyamqp://admin:rabbitmq@<rabbitmq_instance_private_IP>/
* result_backend = db+postgresql://ubuntu@<postgres_instance_private_IP>:5432/airflow
* worker_log_server_port = 8794
```

## Make the run_scheduler_web.sh 

```bash
airflow scheduler
airflow webserver
```

## Variables

Enter the following variables in variable section in Airflow Admin page:

```bash
ethereum_output_bucket=eth-blockchain-airflow
ethereum_classic_output_bucket=eth-blockchain-airflow
ethereum_aws_access_key_id= ?
ethereum_classic_aws_access_key_id=?
ethereum_classic_aws_secret_access_key=?
ethereum_aws_secret_access_key=?
ethereum_provider_uri=https://mainnet.infura.io
ethereum_backup_provider_uri=<backup_uri>
ethereum_classic_provider_uri=https://ethereumclassic.network
ethereum_cloud_provider=aws
cloud_provider=aws
```


