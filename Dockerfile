FROM python:3.8-slim-bullseye

WORKDIR /opt/src

COPY requirements.txt .

RUN pip install -r requirements.txt \
    
    && rm -rf /root/.cache/pip

COPY . .

ENTRYPOINT ["./entrypoint.sh"]

