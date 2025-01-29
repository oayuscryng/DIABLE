
# Active Man-in-the-Middle (MitM) Challenge

This repository contains a **Man-in-the-Middle (MITM)** challenge using Docker Compose. It sets up three containers:

1. **Server** – A basic HTTP server that requires Basic Auth and reveals a hidden flag upon correct credentials.
2. **Victim** – Periodically sends HTTP requests (with credentials) to the server.
3. **Attacker** – Equipped with ARP spoofing and packet capture tools. The goal is to intercept traffic and discover the flag.

**The attacker container does not automatically intercept** traffic from the client. Instead, **you** must actively trick or redirect the client so its traffic goes to the attacker container rather than the real server.

You can start by opening a terminal and run :
```sh
docker exec -it attacker bash
```
and enable IP Forwarding to allow the attacker container to forward packets between victim and server:
```sh
echo 1 > /proc/sys/net/ipv4/ip_forward
```

The flag starts by "MITM_Att"