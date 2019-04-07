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

The engineering challenge lies in the heath of the task DAGs. There are 2 main DAGs, namely, export and load DAGs. Ethereum node connection task is related to export DAG which is consist of 3 tasks (refer to the image below). The choice of DAGs architecture is challenging since a not proper choice can lead to unpredicted and imperformant behavior of the ETL process. 

![no_nodewatch_DAG.png](https://github.com/sfermion/NodeWatch/blob/master/docs/images/no_nodewatch_DAG.png)

In order to make the export DAG fault tolerant against ethereum node failure, I first implemented subdags to check the connection in each individual task. However, it is proven that subdags are not compatible with kubernetes platform and they can cause leadlocks. Since, the ethereum-etl-airflow project will be using kubernetes as the main deployment platform, I decided to solve the problem in a different way. For more discussion on this issue please refer to this article. https://www.astronomer.io/guides/subdags/

My second solution and final proposal to this issue is implementing cross-communication (XCOM) feature in airflow to share data within tasks. I developed the NodeWatch task which is in charge of testing the main ethereum node connection at the beginning of the export DAG. If the connection is healthy, it sends a signal to the dependent tasks to use the main node connection otherwise it tells the tasks to use the alternative ethereum node (please refer to the image below).

![nodeWatch_DAG.png](https://github.com/sfermion/NodeWatch/blob/master/docs/images/nodeWatch_DAG.png)


## How to run the project?

In order to run the project, one requires to install Python 3.5+, go-ethereum and ethereum-etl library before starting the to run the airflow workers. Please follow the instruction provided in the link below to setup the required tools and technologies:

* Postgres database as the meta-databade 
* Go-ethereum to start the parity sync
* Celery as the executor
* RabbitMQ as the broker
* Airflow cluster ()
* Setup redshift in AWS

## Data source

The ethereum blockchain data was collected using go-ethereum library which makes a connection either to a parity-synced local machine or an external source, i.e., https://mainnet.infura.io. 

## Pipeline, Architecture and Teckstack

![Architechture_pipeline.png](https://github.com/sfermion/NodeWatch/blob/master/docs/images/Pipeline_techstack.png)