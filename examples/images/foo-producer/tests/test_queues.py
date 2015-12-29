#!/usr/bin/env python

from celery import Celery

app = Celery('tasks')
app.config_from_object('celeryconfig')

def test_queues():
    for q in [None, 'default', 'foo-tasks']:
        yield _test_with_queue, q

def _test_with_queue(queue_name):
    t1 = app.signature('foo.tasks.waste_time', args=(1,))
    r1 = t1.apply_async(queue=queue_name)
    print 'Sent %s on queue <%s>: %r' % (t1, queue_name, r1)
    y1 = r1.get(timeout=12)
    print 'Result of %r: %r' %(r1, y1)
    assert 'status' in y1

    t2 = app.signature('foo.tasks.add', args=(1,5))
    r2 = t2.apply_async(queue=queue_name)
    print 'Sent %s on queue <%s>: %r' % (t2, queue_name, r2)
    y2 = r2.get(timeout=5)
    print 'Result of %r: %r' %(r2, y2)
    assert y2 == 1 + 5
