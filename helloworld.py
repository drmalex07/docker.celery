from celery import Celery
from celery.task import task
from celery.utils.log import get_task_logger

import time

log1 = get_task_logger(__name__)

@task
def greet(name):
    greeting = 'Hello, %s' %(name)
    log1.info(greeting)
    return greeting

@task
def waste_time(n=12):
    '''Emulate a long-running task'''
    for i in range(0, n):
        log1.info('Wasting some time (%d/%d)' % (i, n))
        time.sleep(5)
    log1.info('Finished task')
    return {'status': 'wasted'}

