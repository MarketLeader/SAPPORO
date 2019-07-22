#!/bin/bash
set -eux
wait-for database:5432
python3 /opt/SAPPORO/SAPPORO-web/src/manage.py makemigrations app
python3 /opt/SAPPORO/SAPPORO-web/src/manage.py migrate
python3 /opt/SAPPORO/SAPPORO-web/src/manage.py collectstatic --noinput --clear
uwsgi /opt/SAPPORO/SAPPORO-web/etc/uwsgi/uwsgi.ini
