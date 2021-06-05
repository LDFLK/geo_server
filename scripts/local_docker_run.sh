docker kill local_geo_server
docker rm /local_geo_server
docker run -p 82:82 -d --name local_geo_server nuuuwan/geo_server
docker ps
