#!/bin/bash

SERVER_IP="server"  # We can refer to the container by service name thanks to Docker DNS
USERNAME="victimuser"
PASSWORD="SuperSecretPass"

# Endless loop. The victim attempts to fetch the protected resource every 5 seconds.
while true; do
  echo "Victim trying to access server..."
  curl -s -u "$USERNAME:$PASSWORD" http://$SERVER_IP/ > /dev/null
  sleep 5
done
