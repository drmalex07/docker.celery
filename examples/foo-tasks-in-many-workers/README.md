README
======

Create a group of Celery workers aware of a custom (`foo`) set of tasks. 

We build this example on a simple Vagrant setup that creates all needed containers (a redis queue and a the group of workers).

## Quickstart

Create containers (the Docker image is built in advance):

    vagrant up --no-parallel --provider docker

Send tasks to a `celery-1-n[123]` container.

Print worker's log:

    docker logs celery-1-n1

or attach to it:

    docker attach --sig-proxy=0 celery-1-n1

## Examples

1. Inspect the status of workers. Create an one-off container from same image, and run commands (status, inspect etc.) inside:

    docker run --rm -it \
       -e BROKER_URL=redis://redis/0 -e CELERY_RESULT_BACKEND=redis://redis/1 --link celery-1-redis:redis \
       local/celery:3.1 inspect registered

2. Open a Celery shell and send a chord of tasks (maybe from inside an one-off container). These tasks should be distributed (in a roughly equal manner) to all workers.
For example, let's calculate the sum `1 * 2 + 2 * 3 + ... + i * (i+1) + ...`:

```python
N = 15
add_tasks = (subtask('foo.tasks.add', args=(i,j)) for (i,j) in zip(range(N), range(1, N+1)))
t = chord(add_tasks, subtask('foo.tasks.addi'))
r = t.apply_async(queue='foo')
r.get()
```
