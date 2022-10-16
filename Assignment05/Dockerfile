# base image
FROM python:3.7-slim-buster

# create workdirectory
WORKDIR /opt/src

# copy our requirements
COPY requirements.txt requirements.txt

# install dependencies
RUN pip install -r requirements.txt && rm -rf /root/.cache/pip

# copy this folder contents to image
COPY demo_scripted.py demo_scripted.py
COPY s3_util.py s3_util.py

# tell the port number the container should expose
EXPOSE 80

ENTRYPOINT ["python", "demo_scripted.py"]