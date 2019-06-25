#!/bin/bash

source ~/.bashrc
rm -f /tmp/*.pid

python manage.py migrate
python manage.py collectstatic --noinput

gunicorn events_system.wsgi:application -b 0.0.0.0:8001 --timeout 300 --workers=3 --reload