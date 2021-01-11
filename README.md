# Postgresql docker
## Create docker container
Get postgres 12 docker image.
```
docker pull postgres:12
```

Crate a directory for postgres data and start a container
```
mkdir <a directory path>/recoflix-postgres
docker run -d \
	--name recoflix-postgres \
	-e POSTGRES_PASSWORD=Pass2020! \
	-v <a directory path>/recoflix-postgres/:/var/lib/postgresql/data \
        -p 5432:5432
        postgres:12
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
CREATE USER recoflix_user WITH ENCRYPTED PASSWORD 'recoflix';
GRANT ALL PRIVILEGES ON DATABASE recoflix_user TO recoflix;
```
