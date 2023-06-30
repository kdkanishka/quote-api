FROM jenkins/jenkins:latest
USER root
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget
# Install app dependencies
RUN pip install --upgrade pip
RUN apt-get install -y python3-venv
