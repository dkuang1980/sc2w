#! /bin/bash

DJANGO_SETTINGS_MODULE=sc2w.conf.prod gunicorn sc2w.wsgi -b 127.0.0.1:8000 -w 5
