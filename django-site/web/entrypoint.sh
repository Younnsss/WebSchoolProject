#!/bin/sh

# Exécute les migrations
python manage.py migrate

python manage.py createsuperuser  --noinput

# Démarre le serveur
python manage.py runserver 0.0.0.0:8001
