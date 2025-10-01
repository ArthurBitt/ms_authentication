FROM python:3.13-slim

WORKDIR /application

COPY . .

RUN apt-get update -y && apt-get upgrade -y && \
    apt-get install -y \
        tzdata \
        libpq-dev \
        gcc \
        python3-dev \
        build-essential \
        locales && \
    sed -i '/pt_BR.UTF-8/s/^# //g' /etc/locale.gen && \
    locale-gen pt_BR.UTF-8 && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -rf /var/lib/apt/lists/*

# Define locale global
ENV LANG=pt_BR.UTF-8
ENV LC_ALL=pt_BR.UTF-8