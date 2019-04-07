# Setup an Ethereum node

## Install Geth:
1. sudo apt-get install software-properties-common
2. sudo add-apt-repository -y ppa:ethereum/ethereum
3. sudo apt-get update
4. sudo apt-get install ethereum

5. eth account new
6. pass: {password}

save the generated address
-->Address: {address}

## clone the go-ethereum project

git clone https://github.com/ethereum/go-ethereum

## Install Go
1. sudo apt-get update
2. sudo apt-get -y upgrade
3. cd /tmp
4. wget https://dl.google.com/go/go1.11.linux-amd64.tar.gz
5. sudo tar -xvf go1.11.linux-amd64.tar.gz
6. sudo mv go /usr/local
7. vim ~/.bashrc
	* export GOROOT=/usr/local/go
	* export GOPATH=$HOME/go
	* export PATH=$GOPATH/bin:$GOROOT/bin:$PATH
	* source ~/.bashrc
8. sudo apt-get install -y build-essential
9. cd go-ethereum
10. make geth

## Make a run_node bash file:

1. vim run_etl_node.sh
2. /home/ubuntu/go-ethereum/build/bin/geth
3. chmod +x run_etl_node.sh

## Start syncing process 
* nohup geth --cache=4098 --rpc --rpcaddr 0.0.0.0 &


## Check syncronization
* geth attach
* eth.syncing

