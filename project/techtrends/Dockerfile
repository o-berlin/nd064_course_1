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
RUN echo "echo \$HOME" && echo $HOME
RUN echo "echo \$WORKDIR" && echo $WORKDIR
#RUN pip install -r requirements.txt

#Bug fixed by using this article: https://davidhamann.de/2021/11/09/docker-entrypoint-not-found/
# command to run on container start

RUN ["chmod", "+x", "scripts.sh"]
ENTRYPOINT ['scripts.sh']