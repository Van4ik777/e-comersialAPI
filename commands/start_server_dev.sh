#!/bin/bash

python manage.py migrate
python manage.py check

python manage.py runserver 0:8000