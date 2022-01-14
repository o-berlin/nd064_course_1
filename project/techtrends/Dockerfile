FROM python:2.7
LABEL maintainer="Olga Berlin"
COPY ./project/techtrends /techtrends
WORKDIR /techtrends
#RUN apt-get update
#RUN apt-get install -y python sqlite3 vim
#RUN apt-get install -y python-setuptools python-dev build-essential python-pip
# due to docker issue installing requirements here
RUN pip install flask
RUN pip install werkzeug
RUN echo $pwd
ENTRYPOINT [/techtrends]
#RUN pip install -r requirements.txt

#Bug fixed by using this article: https://davidhamann.de/2021/11/09/docker-entrypoint-not-found/
# command to run on container start
RUN chmod +x ./script.sh
RUN  ./scripts.sh