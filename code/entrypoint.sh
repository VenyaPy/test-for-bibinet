#!/bin/bash
set -e

sleep 5

python manage.py makemigrations
python manage.py migrate
python manage.py populate_initial_data
python manage.py populate_parts

gunicorn --workers=4 --bind=0.0.0.0:8000 bibinet.wsgi:application
