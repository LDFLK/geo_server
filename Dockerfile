FROM python:3.8-slim-buster
WORKDIR /geo_server

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY geo_server.py geo_server.py

EXPOSE 4002
CMD [ "python3", "geo_server.py"]
