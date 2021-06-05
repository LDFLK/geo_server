docker build -t nuuuwan/geo_server .
echo 'Docker build complete. Starting server...'
docker run -p 4002:4002 nuuuwan/geo_server
