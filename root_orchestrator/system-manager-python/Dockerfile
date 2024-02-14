FROM python:3.10-slim-buster
LABEL org.opencontainers.image.source https://github.com/oakestra/oakestra

# The greenlet pip package requires gcc & g++ to work properly.
RUN apt-get update && apt-get install -y --no-install-recommends gcc g++ curl

ADD requirements.txt /

RUN pip install -r requirements.txt --no-cache-dir && rm /requirements.txt

ADD . /

RUN DOCKER_CONFIG=${DOCKER_CONFIG:-$HOME/.docker} &&\
    mkdir -p $DOCKER_CONFIG/cli-plugins &&\
    curl -SL https://github.com/docker/compose/releases/download/v2.24.5/docker-compose-linux-x86_64 -o $DOCKER_CONFIG/cli-plugins/docker-compose &&\
    chmod +x $DOCKER_CONFIG/cli-plugins/docker-compose

# TRUE for verbose logging
ENV FLASK_DEBUG=TRUE

ENV CLOUD_MONGO_URL=localhost
ENV CLOUD_MONGO_PORT=10007

ENV CLOUD_SCHEDULER_URL=localhost
ENV CLOUD_SCHEDULER_PORT=7777

ENV NET_PLUGIN_URL=localhost
ENV NET_PLUGIN_PORT=10100

EXPOSE 10000

CMD ["python", "system_manager.py"]
