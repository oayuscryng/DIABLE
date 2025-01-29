FROM python:3.9-slim

# Create a working directory
WORKDIR /app

# Copy our simple HTTP server script
COPY server_script.py /app/server_script.py

# Expose port 80 for HTTP
EXPOSE 80

# Run the Python HTTP server
CMD ["python", "server_script.py"]
