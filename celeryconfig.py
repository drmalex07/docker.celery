import os
from kombu import Queue, Exchange

## Backends

BROKER_URL = os.environ.get('BROKER_URL', 'amqp://')

CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'rpc://')

## Task serializers

CELERY_TASK_SERIALIZER = 'json'

CELERY_RESULT_SERIALIZER = 'json'

CELERY_ACCEPT_CONTENT = ['json', 'yaml']

## Tasks

CELERY_IMPORTS = os.environ.get('CELERY_IMPORTS').split(';')

## Concurrency

CELERYD_CONCURRENCY = os.environ.get('CELERYD_CONCURRENCY', 4)

## Routing 

CELERY_DEFAULT_EXCHANGE = 'celery'

CELERY_DEFAULT_EXCHANGE_TYPE = 'direct'

CELERY_CREATE_MISSING_QUEUES = True

CELERY_DEFAULT_QUEUE = os.environ.get('CELERY_DEFAULT_QUEUE', 'default')

CELERY_DEFAULT_ROUTING_KEY = os.environ.get('CELERY_DEFAULT_ROUTING_KEY', 'default')

default_exchange = Exchange(CELERY_DEFAULT_EXCHANGE, CELERY_DEFAULT_EXCHANGE_TYPE)
queue_names = os.environ.get('CELERY_QUEUES')
if queue_names:
    # This worker is going to consume from explicitly named queues
    queue_names = set(queue_names.split(";"))
    CELERY_QUEUES = [
        Queue(name, exchange=default_exchange, routing_key=name) for name in queue_names]
