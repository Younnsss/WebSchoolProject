#!/bin/sh

# Exécute les migrations
python manage.py migrate

python manage.py loaddata users.json
python manage.py loaddata videogames.json

export DJANGO_SUPERUSER_USERNAME=root
export DJANGO_SUPERUSER_PASSWORD=pass
export DJANGO_SUPERUSER_EMAIL=myemail@example.com

python manage.py createsuperuser  --noinput

# Démarre le serveur
python manage.py runserver 0.0.0.0:8001
