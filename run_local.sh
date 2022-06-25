#!/bin/bash

python -c 'import secrets; print(secrets.token_urlsafe())' > secret_key.txt
python manage.py migrate

# Uncomment to run local
# python manage.py runserver 0.0.0.0:80

python manage.py runserver
