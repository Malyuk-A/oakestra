FROM python:3.10-slim-buster
LABEL org.opencontainers.image.source https://github.com/oakestra/oakestra

ADD requirements.txt /

RUN pip install -r requirements.txt

ADD . /

# TRUE for verbose logging
ENV FLASK_ENV=development
ENV FLASK_DEBUG=TRUE

ENV ROOT_FL_IMAGE_REGISTRY_INTERNAL_PORT=5000
ENV ROOT_FL_IMAGE_REGISTRY_EXTERNAL_PORT=5073

ENV ROOT_FL_MANAGER_PORT=5072
EXPOSE $ROOT_FL_MANAGER_PORT

CMD ["python", "root_fl_manager.py"]
