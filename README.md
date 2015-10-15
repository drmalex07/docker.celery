# docker.celery


## Quickstart

Build the image:

    docker build -t local/celery .

Start a Redis instance into a container:

    docker run --rm -ti --name redis-1 --hostname redis-1.internal -P redis:3.0

Start a Celery container and link to our Redis instance:

    docker run --rm -ti --name celery-1 --hostname celery-1.internal --link redis-1:redis -e BROKER_URL=redis://redis/0 -e CELERY_RESULT_BACKEND=redis://redis/1 local/celery

