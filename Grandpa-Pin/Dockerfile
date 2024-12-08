# Use the official Python image from Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the Python script into the container
COPY lvl2.py flag.txt pin.txt /app/

# Install netcat for listening on the specified port
RUN apt-get update && apt-get install -y socat && apt-get clean

# Expose port 4002 for communication
EXPOSE 4002

# Run the Python script with netcat to listen on port 4002 and interact with users
CMD ["socat", "tcp-listen:4002,reuseaddr,fork", "exec:'python3 -u /app/lvl2.py'"]
