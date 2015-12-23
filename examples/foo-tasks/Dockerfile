FROM local/celery:3.1

WORKDIR /home/celery

# Install a foo Python package that defines tasks inside foo.tasks module
ADD foo ./foo

USER root
RUN cd foo && python setup.py install

USER celery
ENV CELERY_IMPORTS "foo.tasks"
