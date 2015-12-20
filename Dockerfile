FROM python:2.7-slim

RUN groupadd user && useradd --shell /bin/bash --create-home --home-dir /home/user -g user user
WORKDIR /home/user

RUN pip install redis

ENV CELERY_VERSION 3.1.18

RUN pip install "celery==${CELERY_VERSION}"

ENV BROKER_URL "amqp://guest@rabbit"
ENV CELERY_RESULT_BACKEND "rpc://"
ENV CELERY_RESULT_PERSISTENT 0
ENV CELERY_IMPORTS "helloworld"
ENV CELERYD_CONCURRENCY 4

COPY celeryconfig.py celeryconfig.py

COPY helloworld.py helloworld.py

LABEL name="celery"

USER user
ENTRYPOINT ["celery", "worker"]
CMD ["--loglevel", "INFO"]

