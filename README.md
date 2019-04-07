# NodeWatch

## Introduction

Ethereum blockchain is an open source, public blockchain that enables developers to create and deploy applications such as smart contracts on it. 

Being decentralized and public make ethereum blockchain an appealing source for cryptography researchers, cryptocurrency investors and developers. However, extracting, transforming and loading (ETL) its data to data warehouses and data lakes is a non intuitive and complex process. 

Ethereum-etl is an open source project which address the above mentioned issue and makes the ETL process smooth. It also enables the data ingestion into cloud-based storage which is a popular choice to build an analytical application workflow.

## Problem Statement

Automation and monitoring of the workflow of data migration from ethereum blockchain to a cloud-based storage is possible using ethereum-etl-airflow project which is based on ethereum-etl codebased. Ethereum-etl-airflow implements Apache Airflow technology to automate the process of 1 TB blockchain data ingestion.

## Proposed Solution
This repository, NodeWatch focuses on an open issue in ethereum-etl-airflow project where a failure in the main node if the blockchain can result in failure in the export tasks. Nodewatch, adds an additional task to the export DAGs (Directed Acyclic Graph) that is responsible for watching the main node. If the main node shots down, NodeWatch will make another connection to an alternative blockchain node so that the ETL process will be continued without a failure.

## Engineering challenges


## Data source
The ethereum blockchain data was collected using go-ethereum library which makes a connection either to a parity-synced local machine or an external source, i.e., https://mainnet.infura.io. 

## Tech Stack


## Pipeline and Architecture

## How to run the project?

In order to run the project, one requires to install Python 3.5+, go-ethereum and ethereum-etl library before starting the to run the airflow workers. Please follow the instruction provided in the link below to setup the required tools and technologies:

* Postgres database as the meta-databade 
* Celery as the scheduler
* RabbitMQ as the broker
* Airflow cluster
* Setup redshift in AWS
