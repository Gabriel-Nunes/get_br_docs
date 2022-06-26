#!/bin/bash

python -c 'import secrets; print(secrets.token_urlsafe())' > secret_key.txt
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
python manage.py runserver 0.0.0.0:80