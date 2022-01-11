FROM python:2.7
LABEL maintainer="Olga Berlin"

COPY . /techtrends
WORKDIR /techtrends
RUN apt-get -y install python-pip
RUN pip install -r requirements.txt

# command to run on container start
ENTRYPOINT ["/bin/bash", "scripts.sh"]