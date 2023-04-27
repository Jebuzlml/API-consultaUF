#!/bin/bash

echo 'Comenzando despliegue...'

echo 'Eliminacion de container antiguo'

# make sure demo docker is not running
sudo docker rm $(sudo docker stop $(sudo docker ps -a -q --filter ancestor=api-uf --format="{{.ID}}"))

echo 'Eliminacion de imagen antigua'

# Delete old imgage
sudo docker rmi -f api-uf

echo 'Construccion de imagen nueva'

# build dockerfile
sudo docker build -f dockerfile -t api-uf .

echo 'Creacion y ejecucion de nuevo contenedor'

# run in detached mode
sudo docker run -d --name api-uf -p 666:80 api-uf

# Delete images useless
sudo docker images -f dangling=true -q | xargs docker rmi

# Clean ram

free -h
sudo sync
sudo sysctl -w vm.drop_caches=3

echo 'Despliegue completado!'
