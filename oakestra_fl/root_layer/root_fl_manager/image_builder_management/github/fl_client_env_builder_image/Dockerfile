FROM python:3.13.0a4-slim-bookworm
LABEL org.opencontainers.image.source https://github.com/oakestra/oakestra

RUN apt-get update && apt-get install -y git buildah && rm -rf /var/lib/apt/lists/*

COPY . /
RUN pip install -r requirements.txt


# IMPORTANT!: Seems to need --privileged otherwise errors occur
#CMD ["bash", "-c", "echo hi; buildah --version; buildah pull alpine; buildah images; "]
