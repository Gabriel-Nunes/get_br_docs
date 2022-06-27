#!/bin/bash

cp config/dev-settings.py config/settings.py
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:80
