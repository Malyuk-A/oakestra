FROM python:3.10-slim-buster
LABEL org.opencontainers.image.source https://github.com/oakestra/oakestra

RUN apt-get update && apt-get install -y docker.io && rm -rf /var/lib/apt/lists/*

COPY . /
