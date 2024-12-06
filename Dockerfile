# Base image
FROM python:3.9-slim-bullseye

# Install system dependencies (No longer need libmysqlclient-dev)
RUN apt-get update --allow-releaseinfo-change && \
    apt-get install -y --no-install-recommends \
    gnupg \
    dirmngr \
    python3-dev \
    gcc \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Set work directory
WORKDIR /app

# Expose the port your app will run on
EXPOSE 5010

# Set the default command to run the flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5010"]
