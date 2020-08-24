# pull official base image
FROM python:3.8.3-slim-buster


# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# set environment varibles
ENV COMPOSE_CONVERT_WINDOWS_PATHS=1
# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc \
  && apt-get clean

# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# add app
COPY . .