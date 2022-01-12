FROM python:2.7
LABEL maintainer="Olga Berlin"

COPY . /techtrends
WORKDIR /techtrends
RUN echo pwd
#RUN apt-get update
#RUN apt-get install -y python sqlite3 vim
#RUN apt-get install -y python-setuptools python-dev build-essential python-pip
# due to docker issue installing requirements here
RUN pip install flask
RUN echo pwd
RUN pip install werkzeug
RUN echo pwd
RUN echo $PATH
RUN ["chmod", "+x", "./techtrends/scripts.sh"]
#RUN pip install -r requirements.txt

# command to run on container start
CMD ["/bin/bash","./techtrends/scripts.sh"]