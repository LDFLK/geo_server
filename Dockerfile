FROM python:3.8.11-slim-buster
WORKDIR /geo_server
RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

COPY requirements.txt requirements.txt
RUN apt-get update && apt-get install libgl1 libglib2.0-0 -y
RUN pip3 install -r requirements.txt
COPY geo_server.py geo_server.py

EXPOSE 4002
CMD [ "python3", "geo_server.py"]
