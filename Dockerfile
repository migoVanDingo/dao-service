# Use a Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Update GPG keys and install system dependencies
RUN apt-get update --allow-releaseinfo-change && \
    apt-get install -y --no-install-recommends \
    gnupg \
    dirmngr && \
    apt-key adv --fetch-keys http://ftp-master.debian.org/keys/archive-key-12.asc && \
    apt-key adv --fetch-keys http://ftp-master.debian.org/keys/archive-key-12-security.asc && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    libmysqlclient-dev \
    pkg-config && \
    rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container
COPY . /app

# Install the required Python packages
RUN pip install --no-cache-dir -r require
