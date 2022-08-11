FROM python:3.10.5-slim-buster

WORKDIR /opt/notes-api

RUN apt-get update && apt-get install -y vim
RUN pip install --upgrade pip

# install dependencies
COPY ["requirements.txt", "./"]
RUN pip install -r requirements.txt

# copy project
COPY . .
