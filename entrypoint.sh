#!/bin/bash
uwsgi --http=0.0.0.0:8000 \
--ini uwsgi.ini \
--processes 4 \
--static-map /static=/srv/app/static
--static-map /static/srv/app/bundles
--wsgi-file ./onlineweb4/wsgi.pyd