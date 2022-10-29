# STORI accounts API

FASTAPI end point to process a CSV file and send email to client.

## Table of contents 

- [BeforeYouStart](#BeforeYouStart)
- [Development](#development)
  - [Build](#build)
  - [Run](#run)
- [Usingtheinterface](#AfterRun)


## BeforeYouStart

Please fill SMTP server inputs (server, port, user and password) inside config.yaml file priot you run the docker image
  
## Development

We can make use of several `make` commands to ease the building and testing of our application.

### Build

Using Docker

Using Docker Compose

docker-compose --file docker/docker-compose.yml build


### Run

Using Docker Compose:

```

docker-compose --file docker/docker-compose.yml up 

```

Then go to <http://localhost:3000/>

## AfterRun

To try the send email feature, please use swagger interface:

http://localhost:3000/docs#/default/send_account_details_mail_v1_accounts_send_account_details_mail_post

