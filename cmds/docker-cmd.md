# docker cmd

docker build -t txwl-api:remove-device-v1 .

docker tag txwl-api:remove-device-v1 it-artifactory.yitu-inc.com/docker-local/fp/txwlapi:remove-device-v1


## install docker 
sudo apt install docker.io
docker container update --restart=always

docker load -i

docker save noenv/mongo-exporter | pigz --best -p 32 > noenv/mongo-exporter.tar.gz


docker tag txwl/txwl-api:1.0 it-artifactory.yitu-inc.com/docker-local/fp/txwl-api:1.0


docker rmi `docker images| grep it-artifactory.yitu-inc.com/docker-local/fp | awk '{print $3}'`

docker tag docker-local/fp/txwl-api:1.0 txwl/txwl-api:1.0
docker tag docker-local/fp/txwl-api:1.0 71.74.95.70:5000/txwl/txwl-api:1.0
docker push 71.74.95.70:5000/txwl/txwl-api:1.0



docker save txwl/txwl-data-docking:1.0 | pigz --best -p 32 > txwl-data-docking:1.0.tar.gz