FROM python:3.8-slim-buster
WORKDIR /geo_server

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .

EXPOSE 4002
CMD [ "python", "geo_server.py"]
