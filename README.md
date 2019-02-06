# Crypto API
An API for cryptocurrency alerts.

Build on Django & Django Rest Framework<br>
With use of Celery

## Requirements

* python3
* postgresql
* virtualenv

## Installation

### Configure the environment file
```shell
cp .env.example .env
```
Fill .env file with the required parameters
### Prepare the installation
```shell
pip install -r requirements.txt
```
```shell
python3 manage.py migrate
```
### Launch Django in test environment
```shell
cd crypto
python3 manage.py runserver
```
### Launch Celery
```shell
celery -A crypto worker -B --concurrency=20 --loglevel=info
```

## Use Docker instead
```shell
docker-composer up && docker-compose build -d
```