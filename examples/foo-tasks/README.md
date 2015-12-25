README
======

This an example container that installs and registers a custom (`foo`) set of tasks to celery. 

We build this example on a simple Vagrant setup that creates all needed containers (a redis queue and a celery worker).

## Quickstart

Create containers (the image is built if needed):

    vagrant up --no-parallel --provider docker

Send tasks to `celery-1` container, watch worker's log:

    docker logs celery-1
