# Postgresql docker
## Create docker container
Get postgres docker image.
```
docker pull postgres
```

Crate a directory for postgres data and start a container
```
mkdir <a directory path>/postgres-data
docker run -d \
	--name recoflix-postgres \
	-e POSTGRES_PASSWORD=Pass2021! \
	-v <a directory path>/postgres-data:/var/lib/postgresql/data \
        -p 5432:5432
        postgres
```

## Create a database and user
Login to bash shell
```
docker exec -it dev-postgres bash
```
Run psql
```
psql -U postgres
```

Create a database and a user in psql
```
CREATE DATABASE recoflix;
CREATE USER recoflix_user WITH ENCRYPTED PASSWORD 'recoflix_password';
GRANT ALL PRIVILEGES ON DATABASE recoflix_user TO recoflix;
```
