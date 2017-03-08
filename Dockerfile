FROM ubuntu:14.04
RUN apt-get update
RUN apt-get -y install build-essential libssl-dev libffi-dev python-dev git
RUN apt-get -y install python3 python3-pip
#RUN pip3 install azure azure-cli-core
#RUN git clone https://github.com/Azure/azure-storage-python
#RUN python3 /azure-storage-python/setup.py install
