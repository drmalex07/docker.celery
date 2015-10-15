import os

BROKER_URL = os.environ.get('BROKER_URL', 'amqp://')

CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'rpc://')

CELERY_TASK_SERIALIZER = 'json'

CELERY_RESULT_SERIALIZER = 'json'

CELERY_ACCEPT_CONTENT = ['json', 'yaml']

CELERY_IMPORTS = os.environ.get('CELERY_IMPORTS').split(';')
