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

```bash
sudo apt-get update
sudo apt-get -y upgrade
cd /tmp
wget https://dl.google.com/go/go1.11.linux-amd64.tar.gz
sudo tar -xvf go1.11.linux-amd64.tar.gz
sudo mv go /usr/local
vim ~/.bashrc
	* export GOROOT=/usr/local/go
	* export GOPATH=$HOME/go
	* export PATH=$GOPATH/bin:$GOROOT/bin:$PATH
	* source ~/.bashrc
sudo apt-get install -y build-essential
cd go-ethereum
make geth
```

## Make a run_node bash file:

```bash
vim run_etl_node.sh
/home/ubuntu/go-ethereum/build/bin/geth
chmod +x run_etl_node.sh
```

## Start syncing process 

```bash
nohup geth --cache=4098 --rpc --rpcaddr 0.0.0.0 &
```

## Check syncronization

```bash
eth attach
eth.syncing
```
