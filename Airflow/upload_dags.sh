set -e
set -o xtrace
set -o pipefail

airflow_bucket=${1}

if [ -z "${airflow_bucket}" ]; then
    echo "Usage: $0 <airflow_bucket>"
    exit 1
fi

aws s3 cp -r dags/*  s3://${airflow_bucket}/dags/
