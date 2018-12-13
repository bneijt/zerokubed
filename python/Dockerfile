
FROM python

RUN apt-get update && \
    apt-get -y install libzmq3-dev && \
    pip install pyzmq arrow

COPY main.py /main.py


EXPOSE 5555
ENTRYPOINT /usr/local/bin/python /main.py
