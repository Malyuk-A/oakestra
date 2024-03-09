# IMPORTANT!: Needs to be run with --privileged otherwise errors occur.
# Note: This python version comes with the proper apt listing to install buildah version 1.28.2(+)
# This buildah version is crucial to be able to run its "build" command.
FROM python:3.13.0a4-slim-bookworm
LABEL org.opencontainers.image.source https://github.com/oakestra/oakestra

RUN apt-get update && apt-get install -y git wget buildah && rm -rf /var/lib/apt/lists/*

COPY . /
RUN pip install -r requirements.txt


# https://docs.anaconda.com/free/miniconda/#quick-command-line-install
RUN mkdir -p ~/miniconda3 &&\
    wget https://repo.anaconda.com/miniconda/Miniconda3-py312_24.1.2-0-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh &&\
    bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3 &&\
    rm -rf ~/miniconda3/miniconda.sh &&\
    ~/miniconda3/bin/conda init bash &&\
    echo "\nconda deactivate" >> ~/.bashrc
