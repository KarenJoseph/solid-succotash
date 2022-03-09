# solid-succotash
Simple BE for buying items and showing all bought items - using MongoDB Kafka and Python flusk


## Start App
Clone the repo and run
```sh
docker-compose -f docker-compose.yaml up 
```
webserver api is accessible on port 5000

## Use App
### Buy Item
"buy" an item by sending the api
```
POST /buy
```
#### Requested JSON object
username

userid

price

timestamp


For example:
```sh
curl http://localhost:5000/buy -d '{ "username": "AvivT", "userid": "cdj_ks7393cs", "price": "25.6", "timestamp": "67832804329" }'
```
### Get All items
```
GET /allBuys
```
For example:
```sh
curl http://localhost:5000/allBuys
```

## Project Structure
.

├── customer-management

│   ├── api.py >>> api for internal use - called by webserver api

│   ├── consumer.py >>> kafka consumer code

│   ├── Dockerfile

│   └── start.sh >>> helper script to allow running both processes - api server and consumer

├── customer-webserver

│   ├── api.py >>> api exposed to user

│   └── Dockerfile

└── docker-compose.yaml


## TODO
1. Support more than one user - getting all db entries matching a requested id (/allBuys?<userid>)
2. change default db user password and be used as env vars instead of hardcode
3. kafka should be configured as cluster, think about # of partitions
