FROM python:2.7-slim

RUN groupadd user && useradd --shell /bin/bash --create-home --home-dir /home/user -g user user
WORKDIR /home/user

RUN pip install redis

ENV CELERY_VERSION 3.1.18

RUN pip install "celery==${CELERY_VERSION}"

ENV BROKER_URL "amqp://guest@rabbit"

COPY celeryconfig.py celeryconfig.py

USER user
ENTRYPOINT ["celery", "worker"]

