# Shortcut2.work

## Prerequisites
  * Install Docker (Mac: https://docs.docker.com/docker-for-mac/install/, Windows: https://docs.docker.com/docker-for-windows/install/)
  * Install Python3.7+ (https://www.python.org/downloads/)
  * Install docker compose (`pip install docker-compose`)
  * Install Code Editor (Atom: https://flight-manual.atom.io/getting-started/sections/installing-atom/)
  
## Build docker image
```
  docker-compose build
```

## Run dev stack
```
  docker-compose run --service-ports  --rm web
  
  # inside the container
  sh dev_server.sh
```
Then visit http://localhost:8000 on your browser, you should be the webapp UI.
