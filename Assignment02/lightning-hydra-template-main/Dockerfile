# base image
FROM python:3.8-slim

# create workdirectory
WORKDIR /workspace/project

# copy our requirements
COPY requirements.txt requirements.txt

# install dependencies
RUN python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

# copy this folder contents to image
COPY . .
