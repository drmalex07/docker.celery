from celery import Celery
from celery.task import task, subtask
from celery.utils.log import get_task_logger

import time

log1 = get_task_logger(__name__)

class FooError(Exception): pass

@task
def fail():
    raise FooError('Something is wrong')

@task
def add(x, y):
    log1.info ('Adding %.2f and %.2f' %(x,y))
    # calculate and return 
    return x + y

@task
def adda(*args):
    '''A simple task adding all arguments'''
    log1.info('Adding numbers ' + repr(args))
    return sum(args)

@task
def addi(it):
    '''A simple task adding all items from iterable'''
    log1.info('Adding numbers ' + repr(it))
    return sum(it)

@task
def mul(x, y):
    log1.info('Multiplying %.2f and %.2f' %(x,y))
    return x * y

@task
def waste_time(n=12, callback=None): 
    '''Emulate a long-running task'''

    for i in range(0, n):
        log1.info('Wasting some time (%d/%d)' % (i, n))
        time.sleep(5)
    
    if callback:
        log1.info('Finished task: About to invoke %r' % (callback))
        subtask(callback).delay()
    else:
        log1.info('Finished task')
    
    return {'status': 'wasted'}

