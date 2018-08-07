# Shortcut2.work

## Prerequisites
  * Install Docker (Mac: https://docs.docker.com/docker-for-mac/install/, Windows: https://docs.docker.com/docker-for-windows/install/)
  * Install Python3.7+ (https://www.python.org/downloads/)
  * Install docker compose (`pip install docker-compose`)
  * Install Code Editor (Atom: https://flight-manual.atom.io/getting-started/sections/installing-atom/)
  
## Run dev stack
```
  docker-compose up
```
Then visit http://localhost:8000 on your browser, you should be the webapp UI.

## SSH into docker container
```
  sh ssh_into_container.sh
```