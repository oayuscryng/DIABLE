FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y curl

COPY victim_script.sh /app/victim_script.sh
RUN chmod +x /app/victim_script.sh

CMD ["/app/victim_script.sh"]
