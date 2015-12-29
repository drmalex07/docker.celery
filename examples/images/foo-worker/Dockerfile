FROM local/celery:3.1

# Install Python package that defines tasks inside foo.tasks module
ADD foo /opt/foo

USER root
RUN cd /opt/foo && pypy setup.py install

USER celery
ENV CELERY_IMPORTS "foo.tasks"
