FROM python:3
USER root

# Install ffmpeg
RUN apt-get update
RUN apt-get -y install -y vim less
RUN apt-get install -y ffmpeg

# remove cache
RUN rm -rf /var/lib/apt/lists/*

# mount volume
RUN mkdir -p /root/YtExtract
COPY requirements.txt /root/YtExtract
WORKDIR /root/YtExtract

# install python packages
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools    
RUN pip install -r requirements.txt