FROM python:3.7

# set home directory of the project
ENV PROJECT_HOME /opt/sc2w

# expose the port of the django server
EXPOSE 8000

# copy everything in the current repo to project home
COPY . $PROJECT_HOME

# change the current working dir to project home
WORKDIR $PROJECT_HOME

# apt-get update
RUN apt-get update -y 

# apt-get install
RUN apt-get install -y git nano curl iputils-ping netcat dos2unix

# pip install dependencies
RUN pip install -r requirements.txt

# start server
ENTRYPOINT ["/bin/bash", "/opt/sc2w/prod_server.sh"]
