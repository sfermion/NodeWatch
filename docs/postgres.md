## Install postgres

```bash
sudo apt-get install postgresql postgresql-contrib
sudo -u postgres psql
CREATE ROLE ubuntu;
CREATE DATABASE airflow;
GRANT ALL PRIVILEGES on database airflow to ubuntu;
ALTER ROLE ubuntu SUPERUSER;
ALTER ROLE ubuntu CREATEDB;
ALTER ROLE "ubuntu" WITH LOGIN;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public to ubuntu;
```

## change listen_addresses
```bash
sudo vim /etc/postgresql/<int>/main/postgresql.conf
	* edit listen_addresses = '*'
sudo service postgresql restart
sudo service postgresql reload
sudo vim /etc/postgresql/<int>/main/pg_hba.conf 	
	* change the ipv4 address to 0.0.0.0/0 and the ipv4 connection method from md5 (password) to trust
sudo service postgresql restart
sudo service postgresql reload
```

## Connect to DB 

```bash
psql -d airflow
\conninfo
```


