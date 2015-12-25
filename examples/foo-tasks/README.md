README
======

This an example container that installs and registers a custom (`foo`) set of tasks to celery. 

We build this example on a simple Vagrant setup that creates all needed containers (a redis queue and a celery worker).

## Quickstart

Create containers (the image is built if needed):

    vagrant up --no-parallel --provider docker

Send tasks to `celery-1` container, watch worker's log:

    docker logs celery-1

Create an one-off container to inspect status of spawned Celery worker:

    docker run -it --rm \
       -e BROKER_URL=redis://redis/0 -e CELERY_RESULT_BACKEND=redis://redis/1 --link celery-1-redis:redis
       local/celery:3.1 inspect registered
