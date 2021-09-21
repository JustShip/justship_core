# pull the official base image
FROM python:3.8.3-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip 
COPY ./requirements /usr/src/app
RUN pip install -r develop.txt

# copy project
COPY . /usr/src/app


# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]