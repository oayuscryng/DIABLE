# Active Man-in-the-Middle (MitM) Challenge

This project demonstrates an **Active Man-in-the-Middle (MitM) attack** using Docker Compose. The goal is to showcase how an attacker can intercept and manipulate traffic between a victim and a server.

## Features

- **Network Interception:** A Docker-based setup simulating a MitM attack scenario.
- **Basic Authentication Bypass:** Capturing and decoding HTTP Basic Auth credentials.
- **Active Packet Manipulation:** The attacker container can forward and modify traffic between the victim and the server.

## Prerequisites

- **Docker & Docker Compose:** Install Docker on your machine.
- **Linux/macOS (Recommended):** This setup is optimized for Unix-based systems.

## Installation

Clone the repository:
```bash
git clone https://github.com/your-repo/mitm_challenge.git
cd mitm_challenge
```

Build and run the Docker containers:
```bash
docker-compose up --build
```

This will start three containers:
- **Server:** A basic HTTP server requiring authentication.
- **Victim:** Periodically sends requests (with credentials) to the server.
- **Attacker:** Equipped with ARP spoofing and packet capture tools.

## Usage

### 1. Access the Attacker Container
Open a terminal and run:
```bash
docker exec -it attacker bash
```

### 2. Enable IP Forwarding
To allow the attacker container to forward packets between the victim and server, run:
```bash
echo 1 > /proc/sys/net/ipv4/ip_forward
```

### 3. Perform ARP Spoofing & Packet Capture
Use `arpspoof` to trick the victim into sending traffic through the attacker:
```bash
arpspoof -i eth0 -t <Victim-IP> <Server-IP>
```
Capture packets using `tcpdump`:
```bash
tcpdump -i eth0 -A
```

### 4. Extract the Flag
Monitor the captured traffic for HTTP Basic Auth credentials. The hidden flag starts with:
```bash
MITM_Att
```

## Observing the Results

- **If successful:** You will capture authentication credentials and extract the flag.
- **If the attack fails:** The victim may have security measures like HTTPS, preventing interception.

## Risks and Mitigations

- **Risks:**
  - Credential Theft: Attackers can steal usernames and passwords.
  - Data Manipulation: Altering traffic can mislead users.
  - Service Disruption: ARP poisoning can cause network outages.

- **Mitigations:**
  - Use HTTPS: Encrypt communication to prevent eavesdropping.
  - Enable ARP Spoofing Protection: Configure network devices to detect and prevent ARP attacks.
  - Use VPNs: Encrypt all traffic to prevent local network interception.
  - Implement Network Monitoring: Detect suspicious ARP and traffic patterns.

This challenge is designed to help security professionals understand and defend against real-world MitM attacks.

