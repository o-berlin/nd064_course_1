FROM python:2.7
LABEL maintainer="Olga Berlin"

COPY . /techtrends
WORKDIR /techtrends
#RUN apt-get update
#RUN apt-get install -y python sqlite3 vim
#RUN apt-get install -y python-setuptools python-dev build-essential python-pip
# due to docker issue installing requirements here
RUN pip install flask
RUN pip install werkzeug
#RUN pip install -r requirements.txt

# command to run on container start
CMD ["/bin/bash", "./scripts.sh"]