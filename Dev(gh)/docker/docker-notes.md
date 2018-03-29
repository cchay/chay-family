# Docker

# Installing docker in linux:
wget -q0- https://get.docker.com/ | sh

# Docker Notes
* Container vs SErvice
  * Container is deploying single instance of docker image onto single docker host
  * Service is, in auto load balanced environment, multiple docker images spread across multiple swarm nodes

# Docker Engine
Does(90% of docker work)
* >docker build
  * builds an image
  * docker build -t NameOfImage
    * builds and tags and image called "NameOfImage"
* >docker run
  * creates a container from an image and runs it
* >docker logs
  * shows the logs from a container
* >docker ps
  * shows what's running
* >docker stop
* >docker push
* >docker pull
  
# Docker-Compose
Describes the components of the application
* yaml config
  * web container
  * db container
* >docker-compose up
  * starts all of the containers
* >docker-compose build
  * rebuilds your images
* >docker-compose stop
  * stopps the containers

# Docker Machine
Provisions and manages Docker hosts
  * >docker-machine create
    * Creates a new Docker host
  * docker-machine ssh
    * connects to the host using SSH
  * >docker-machine rm
    * destroys the host
  * >docker-machine env
    * sets environment variables for your client to connect to the host
