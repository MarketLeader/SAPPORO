#!/bin/bash
set -eux
wait-for database:5432
python3 /opt/SAPPORO/SAPPORO-web/src/manage.py makemigrations app
python3 /opt/SAPPORO/SAPPORO-web/src/manage.py migrate
uwsgi /opt/SAPPORO/SAPPORO-web/etc/uwsgi/uwsgi.ini
