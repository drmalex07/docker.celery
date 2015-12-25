FROM local/celery:3.1

# Install a foo Python package that defines tasks inside foo.tasks module
ADD foo /opt/foo

USER root
RUN cd /opt/foo && python setup.py install

USER celery
ENV CELERY_IMPORTS "foo.tasks"
