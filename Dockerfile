# Base image
FROM python:3.9-slim-bullseye

# Install system dependencies
RUN apt-get update --allow-releaseinfo-change && \
    apt-get install -y --no-install-recommends \
    gnupg \
    dirmngr \
    libmysqlclient-dev \
    python3-dev \
    gcc \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Set work directory
WORKDIR /app


EXPOSE 5010

CMD ["flask", "run", "--host=0.0.0.0", "--port=5010"]
