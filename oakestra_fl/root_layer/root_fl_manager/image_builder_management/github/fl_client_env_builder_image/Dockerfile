# IMPORTANT!: Needs to be run with --privileged otherwise errors occur.
# Note: This python version comes with the proper apt listing to install buildah version 1.28.2(+)
# This buildah version is crucial to be able to run its "build" command.
FROM python:3.13.0a4-slim-bookworm
LABEL org.opencontainers.image.source https://github.com/oakestra/oakestra

RUN apt-get update && apt-get install -y git wget buildah && rm -rf /var/lib/apt/lists/*

COPY . /
RUN pip install -r requirements.txt
