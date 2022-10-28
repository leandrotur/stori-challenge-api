# STORI accounts API

FASTAPI end point to process a CSV file and send email to client.

## Table of contents 

- [Development](#development)
  - [Build](#build)
  - [Run](#run)
  
## Development

We can make use of several `make` commands to ease the building and testing of our application.

### Build

Using Docker

Using Docker Compose

docker-compose --file docker/docker-compose.yml build


### Run

Using Docker

docker run universe-builder-api:local app start
```

Using Docker Compose

```

docker-compose --file docker/docker-compose.yml up

```

Then go to <http://localhost:3000/>

