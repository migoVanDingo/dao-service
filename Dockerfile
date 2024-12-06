FROM python:3.9-slim-bullseye

WORKDIR /app

# Fixing repository signature errors by using trusted repositories
RUN apt-get update --allow-releaseinfo-change && \
    apt-get install -y --no-install-recommends \
    gnupg dirmngr && \
    echo "deb [trusted=yes] http://deb.debian.org/debian bullseye main" > /etc/apt/sources.list && \
    echo "deb [trusted=yes] http://deb.debian.org/debian-security bullseye-security main" >> /etc/apt/sources.list && \
    echo "deb [trusted=yes] http://deb.debian.org/debian bullseye-updates main" >> /etc/apt/sources.list && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc libmysqlclient-dev pkg-config && \
    rm -rf /var/lib/apt/lists/*

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5010

CMD ["flask", "run", "--host=0.0.0.0", "--port=5010"]
