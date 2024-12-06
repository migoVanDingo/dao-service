# Use a Python base image based on Debian Bullseye
FROM python:3.9-slim-bullseye

# Set the working directory inside the container
WORKDIR /app

# Update GPG keys and install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gnupg \
    dirmngr && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    libmysqlclient-dev \
    pkg-config && \
    rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container
COPY . /app

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Flask will run on
EXPOSE 5010

# Command to run the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5010"]
