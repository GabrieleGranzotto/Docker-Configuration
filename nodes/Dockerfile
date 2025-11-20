# Usa l’immagine ufficiale Ubuntu 24.04
FROM ubuntu:24.04

# Imposta variabili ambientali per evitare prompt interattivi in apt-get
ENV DEBIAN_FRONTEND=noninteractive \
    TZ=Europe/Rome

# Aggiorna e installa i pacchetti necessari
RUN apt-get update && apt-get install -y --no-install-recommends \
    nano vim curl wget build-essential \
    software-properties-common \
    # strumenti per benchmark
    hpcc mpich stress-ng sysbench iozone3 iperf3 netcat-openbsd \
    # pacchetto ssh e settaggi
    openssh-server\
    && mkdir /var/run/sshd \
    && echo 'root:$(openssl rand -base64 12)' | chpasswd \
    && sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config \
    && sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Porta standard ssh
EXPOSE 22

COPY ./misc/scripts/setup.sh /root/setup.sh

RUN chmod +x /root/setup.sh 

WORKDIR /root

COPY ./misc/data/hpccinf.txt /root/hpccinf.txt

# ssh in foreground
CMD ["/bin/bash", "-c", "/root/setup.sh && /usr/sbin/sshd -D"]
