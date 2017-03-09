FROM python:3
RUN apt-get update
RUN git clone https://github.com/Azure/azure-cli
WORKDIR ./azure-cli
RUN python scripts/dev_setup.py
COPY kube-config /root/.kube/config
RUN mkdir /src
WORKDIR /src

