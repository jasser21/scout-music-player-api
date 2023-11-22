#!/usr/bin/env bash
# exit on error
set -o errexit
source ../bin/activate
python manage.py makemigrations
python manage.py collectstatic --no-input
python manage.py migrate
python manage.py runserver