FROM local/celery:3.1

USER root
RUN pip install nose

USER celery
WORKDIR /home/celery
ADD tests tests

ENTRYPOINT ["nosetests"]
CMD ["-v", "tests"]

#ENTRYPOINT ["celery"]
#CMD ["events"]
