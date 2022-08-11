# Notes API

REST API that allows users to manage their notes.  
Notes are organized into folders for easier management.  
API allows user authentication through basic HTTP authentication (username and password).  

# Credentials

All existing credentials can be seen in the [test file](../notes_api/tests/test_notes_api.py).

There are three users configured, with their username:password:
- Bill10:pass10
- Jack20:pass20
- Lara30:pass30

## Adding new users

### Option 1
To add new users it's possible to modify [test_notes_api.py](../notes_api/tests/test_notes_api.py) and to recreate containers with docker-compose:
```
docker-compose down -v
docker-compose up -d --build
```

### Option 2
Create new user by using signup endpoint, no authentication needed. The simplest way is to use [Swagger](http://localhost:5000):
```
http://localhost:5000
```
or to use following curl command:
```
curl -X 'POST' \
  'http://localhost:5000/auth/signup' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "<name>",
  "username": "<username>",
  "password": "<password>"
}'
```

# Database

For database is used Postgres. Tables are automatically created by using docker-compose command.  
Table data is populated through tests, the same way as users and their credentials.

# Setup

Make sure the following ports on your local system are not used:  
- 5000 for the notes-api server
- 5432 for postgres

Run command:
```
docker-compose up -d --build
```

In case if you are unfimiliar with using Swagger UI better [read before](https://idratherbewriting.com/learnapidoc/pubapis_swagger.html).

[Swagger](http://localhost:5000) can be accessed:
```
http://localhost:5000
```

# Tests
All the content in the **tests/api_client** is auto generated from the **swagger.json** by using online [Swagger Editor](https://editor.swagger.io/).

## Remove all the data from database
```
docker exec -it notes-api-test pytest tests -m "teardown"
```

## Set mock data
```
docker exec -it notes-api-test pytest tests -m "teardown" && \
docker exec -it notes-api-test pytest tests -m "mockdata"
```

## Run all tests
```
docker exec -it notes-api-test pytest tests -m "teardown" && \
docker exec -it notes-api-test pytest tests
```

# Other commands
Some of these commands are already part of docker-compose. They are here only as an information to understand better how the system works.

## Create migrations folder
```
flask db init
```

## Create migration file
```
flask db migrate -m "Initial migration."
```

## Apply migrations to DB
```
flask db upgrade
```

## Run Notes API
```
flask run
```
