import os

BROKER_URL = os.environ.get('BROKER_URL', 'amqp://')

CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'amqp://')

CELERY_ACCEPT_CONTENT = ['json', 'yaml']
