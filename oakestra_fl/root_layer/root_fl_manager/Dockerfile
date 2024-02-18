FROM python:3.10-slim-buster
LABEL org.opencontainers.image.source https://github.com/oakestra/oakestra

ADD requirements.txt /

RUN pip install -r requirements.txt

ADD . /

ENV FL_ROOT_MANAGER_PORT=5072
#EXPOSE $FL_ROOT_MANAGER_PORT
EXPOSE 5072

CMD ["python", "root_fl_manager.py"]
