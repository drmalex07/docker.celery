README foo-producer
===================

An example image for a container that produces (i.e. sends) `foo` tasks to a broker (from where a group of celery workers will consume them).

Note that a producer only needs to know the signature of tasks that sends (via a broker) to workers. So, the actual task library is not present
in this image (i.e you can only `apply_async()` or `delay()` tasks, but you cannot `apply()` because the later requires task's code to be present
in this machine).
