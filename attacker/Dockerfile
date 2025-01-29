FROM ubuntu:22.04

# Install tools needed for ARP spoofing and packet capturing
RUN apt-get update && \
    apt-get install -y dsniff tcpdump iproute2 iputils-ping && \
    apt-get clean

CMD ["/bin/bash"]
