# base image
FROM python:3.8-slim

# create workdirectory
WORKDIR /app

# copy our requirements
COPY requirements.txt requirements.txt

# install dependencies
RUN python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

# copy this folder contents to image
COPY . .

# tell the port number the container should expose
EXPOSE 5000

ENTRYPOINT ["python", "./src/train.py"]