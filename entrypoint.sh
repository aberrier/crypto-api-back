#!/bin/sh

python manage.py migrate
exec gunicorn -w 4 --log-level=info --access-logfile=- --error-logfile=- -b 0.0.0.0:8000 crypto.wsgi


exec "$@"
