#!/usr/bin/env python

from celery import Celery
from celery import chain, chord

app = Celery('tasks')
app.config_from_object('celeryconfig')

queue_name = 'foo-tasks'

def test_chord():
    
    # Compute the sum: xv[1] * yv[1] + ... + xv[N] * yv[N]
    xv = (1, 5, 3, 2, 6, 7, 1)
    yv = (5, 1, 2, 2, 1, 2, 7)

    multiplications = (
        app.signature('foo.tasks.mul', args=(x, y)) for x, y in zip(xv, yv))
    addition = app.signature('foo.tasks.addi', args=()) # will receive vector of chord tasks
    t1 = chord(multiplications, addition)
    r1 = t1.apply_async(queue=queue_name)
    print 'Sent %s on queue <%s>: %r' % (t1, queue_name, r1)
    y1 = r1.get(timeout=10)
    print 'Result of %r: %r' %(r1, y1)
    assert y1 == sum([x * y for (x, y) in zip(xv, yv)])

def test_chain():
    t11 = app.signature('foo.tasks.mul', args=(2, 3))
    t12 = app.signature('foo.tasks.add', args=(1,)) # receives as 2nd arg the result of t11
    t13 = app.signature('foo.tasks.add', args=(3,)) # receives as 2nd arg the result of t12
    t1 = chain(t11, t12, t13)
    r1 = t1.apply_async(queue=queue_name)
    print 'Sent %s on queue <%s>: %r' % (t1, queue_name, r1)
    y1 = r1.get(timeout=10)
    print 'Result of %r: %r' %(r1, y1)
    assert y1 == 2 * 3 + 1 + 3

