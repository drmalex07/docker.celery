FROM local/celery:3.1

WORKDIR /home/user

# Install a foo Python package that defines tasks inside foo.tasks module
ADD foo ./foo

USER root
RUN cd foo && python setup.py install

USER user
ENV CELERY_IMPORTS "foo.tasks"
