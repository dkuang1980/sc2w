#! /bin/bash

python manage.py migrate --settings=sc2w.conf.dev

python manage.py runserver --settings=sc2w.conf.dev 0.0.0.0:8000