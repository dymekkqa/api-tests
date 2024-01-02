FROM python:3.9.7-alpine3.14


RUN echo "https://dl-4.alpinelinux.org/alpine/v3.10/main" >> /etc/apk/repositories && \
    echo "https://dl-4.alpinelinux.org/alpine/v3.10/community" >> /etc/apk/repositories


RUN apk update && \
    apk add openjdk11-jre curl tar


RUN curl -o allure-2.10.0.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.10.0/allure-commandline-2.10.0.tgz && \
    tar -zxvf allure-2.10.0.tgz -C /opt/ && \
    ln -s /opt/allure-2.10.0/bin/allure /usr/bin/allure && \
    rm allure-2.10.0.tgz

WORKDIR /usr/workspace


COPY ./requirements.txt /usr/workspace
RUN pip3 install -r requirements.txt


RUN pip3 install pytest


