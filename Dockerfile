# Use alpine images to keep size small
# https://mherman.org/presentations/dockercon-2018/#33
FROM python:3.8.3-alpine

# WORKDIR is inside the container
WORKDIR /blogsite

ENV PYTHONUNBUFFERED=1

# Install Pillow dependencies
RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers 

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
