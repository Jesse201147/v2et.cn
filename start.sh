#! /bin/bash

python manage.py collectstatic --noinput&&
python manage.py makemigrations&&
python manage.py migrate&&
gunicorn v2et.wsgi:application -c config/gunicorn.conf
