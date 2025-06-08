FROM docker.io/python:latest
# Set working directory
WORKDIR /app
RUN apt-get update && apt-get install -y bash
# Copy everything into the image
COPY . .

# Install dependencies
RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 freeze