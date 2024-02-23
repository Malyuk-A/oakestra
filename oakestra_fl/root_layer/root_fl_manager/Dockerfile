FROM python:3.10-slim-buster
LABEL org.opencontainers.image.source https://github.com/oakestra/oakestra

RUN apt-get update && apt-get install git -y && apt-get clean

ADD requirements.txt /

RUN pip install -r requirements.txt

ADD . /

# TRUE for verbose logging
ENV FLASK_ENV=development
ENV FLASK_DEBUG=TRUE

ENV ROOT_FL_IMAGE_REGISTRY_PORT=5073
ENV ROOT_FL_MANAGER_PORT=5072
EXPOSE $ROOT_FL_MANAGER_PORT

ENV ROOT_MQTT_BROKER_PORT=9027
ENV ROOT_MQTT_BROKER_URL=root_mqtt

CMD ["python", "root_fl_manager.py"]
