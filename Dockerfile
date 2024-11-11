FROM python:3
USER root

RUN apt-get update
RUN apt-get -y install -y vim less

RUN mkdir -p /root/YtExtract
COPY requirements.txt /root/YtExtract
WORKDIR /root/YtExtract

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools    
RUN pip install -r requirements.txt