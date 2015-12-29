FROM local/celery:3.1

USER root
RUN pip install flower

USER celery
WORKDIR /home/celery

CMD ["flower"]
