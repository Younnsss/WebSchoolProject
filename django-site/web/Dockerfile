# docker build --build-arg http_proxy="http://proxy-infra.pin.dolmen.bouyguestelecom.fr:3128" --build-arg https_proxy="http://proxy-infra.pin.dolmen.bouyguestelecom.fr:3128" --build-arg no_proxy=".bouyguestelecom.fr,nbyt.fr" -t djangoapp .
FROM registry.glouton.int.nbyt.fr/python:latest

WORKDIR /app

COPY . /app

RUN chmod +x /app/entrypoint.sh

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["/bin/sh", "/app/entrypoint.sh"]
