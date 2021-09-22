# pull the official base image
FROM python:3.8-slim

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip 
COPY ./requirements /usr/src/app
RUN pip install -r production.txt

# copy project
COPY . /usr/src/app
RUN chmod +x /usr/src/app/docker-entrypoint.sh

ENTRYPOINT [ "/usr/src/app/docker-entrypoint.sh" ]
