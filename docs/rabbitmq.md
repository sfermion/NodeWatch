## Install RabbitMQ

```bash
sudo apt-get update
sudo apt-get install rabbitmq-server
sudo vim /etc/rabbitmq/rabbitmq-env.conf
	* NODE_IP_ADDRESS=0.0.0.0
```

## Start RabbitMQ

```bash
sudo service rabbitmq-server start
```

## Make Admin User
```bash
sudo rabbitmq-plugins enable rabbitmq_management
sudo rabbitmqctl add_user admin rabbitmq
sudo rabbitmqctl add_vhost dev
sudo rabbitmqctl set_user_tags admin administrator
sudo rabbitmqctl set_permissions -p / admin ".*" ".*" ".*"
sudo rabbitmqctl set_vm_memory_high_watermark 0.8
sudp abbitmqctl set_policy Lazy "^lazy-queue$" '{"queue-mode":"lazy"}' --apply-to queues
ulimit -n 65535
```
