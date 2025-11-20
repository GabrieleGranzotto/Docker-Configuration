# Usa l’immagine ufficiale Ubuntu 24.04
FROM ubuntu:24.04

# Imposta variabili ambientali per evitare prompt interattivi in apt-get
ENV DEBIAN_FRONTEND=noninteractive \
  TZ=Europe/Rome

# Aggiorna e installa i pacchetti necessari
RUN apt-get update && \
  apt-get install -y --no-install-recommends \
  nano vim curl wget build-essential \
  software-properties-common \
  # strumenti per benchmark
  hpcc mpich stress-ng sysbench iozone3 iperf3 netcat-openbsd \
  # per connettersi con ssh
  openssh-client \
  && apt-get clean && rm -rf /var/lib/apt/lists/*

# Crea la chiave ssh
RUN ssh-keygen -f /root/.ssh/id_rsa -N "" \
    && echo "Host *" > /root/.ssh/config \
    && echo "    StrictHostKeyChecking no" >> /root/.ssh/config \
    && echo "    UserKnownHostsFile /dev/null" >> /root/.ssh/config \
    && chmod 600 /root/.ssh/config

WORKDIR /root/

COPY ./misc/data/hpccinf.txt /root/hpccinf.txt
COPY ./misc/scripts/docker_iozone_script.sh /root/iozone_script.sh

# Comando di default: entra in shell
CMD ["/bin/bash", "-c", "cp /root/.ssh/id_rsa.pub /data/ && sleep infinity"]
