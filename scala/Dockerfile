
FROM openjdk

RUN apt-get update && \
    apt-get -y install libzmq-java

COPY build/libs /libs

WORKDIR /libs
ENTRYPOINT /usr/bin/java -jar app.jar
