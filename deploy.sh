#!/bin/sh

# python3 ./core/manage.py collectstatic --settings=config.settings.develop --noinput
docker-compose -f production.yml up -d --build
