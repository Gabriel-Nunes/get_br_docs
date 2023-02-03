#!/bin/sh

python manage.py migrate
python manage.py collectstatic --noinput --clear

gunicorn config.wsgi:application --bind 0.0.0.0:8000
# python manage.py runserver 0.0.0.0:8000