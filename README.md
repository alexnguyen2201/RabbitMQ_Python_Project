# RabbitMQ_Python_Project

## Build and Run Container
![Screen Shot 2022-05-15 at 12 53 15](https://user-images.githubusercontent.com/53045534/168459174-de3d3f03-de3b-4bd4-8c58-15f8eedcc6a5.png)

### Build containers
```console
docker-compose build
```
### Create network
```console
docker network create "ihddocker"
```
### Run containers
```console
docker-compose up --scale restaurant-service=2
```
![Screen Shot 2022-05-15 at 12 56 28](https://user-images.githubusercontent.com/53045534/168459250-9300bbeb-881c-458d-857e-c4a711c4f508.png)

## Create Database
```console
docker exec -it rabbitmq-python-project-mysql-1 /bin/sh
mysql -u root -p
GRANT ALL PRIVILEGES ON *.* TO 'test'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
CREATE DATABASE food;
use food;
```

## Create Models and Tables for Databse
```console
docker exec -it rabbitmq-python-project-order-service-1 /bin/sh
alembic upgrade head
```
## Observe Logs

Open logs for 2 restaurant-service
Open 2 terminal, use command:
- Terminal 1
```console
docker container logs -f rabbitmq-python-project-restaurant-service-1
```
- Terminal 2
```console
docker container logs -f rabbitmq-python-project-restaurant-service-2
```
Or we can see logs of all container at `docker-compose up --scale restaurant-service=2 terminal`

## Use API
Open browser: http://localhost:3000/docs 

Creat item first:
Use API POST `/api/v1/item/`
body request:
```json
{
  "name": "apple",
  "price": 10
}
```
Use API POST `/api/v1/item/`
body request:
```json
{
  "name": "orange",
  "price": 20
}
```
Use API POST `/api/v1/item/`
body request:
```json
{
  "name": "banana",
  "price": 30
}
```


Create Ordrer:
USE API POST `/api/v1/order/`
body request:
```json
{
  "email": "user@example.com",
  "items": [
    {
      "id": 1,
      "quantity": 2
    },
    {
      "id": 2,
      "quantity": 5
    }
  ]
}
```
