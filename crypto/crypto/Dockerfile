FROM python:3.6

COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

COPY . /app
WORKDIR /app/crypto

ENTRYPOINT celery -A crypto worker -B --concurrency=20 --loglevel=info
