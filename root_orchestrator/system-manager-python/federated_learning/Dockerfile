FROM python:3.10-slim-buster
LABEL org.opencontainers.image.source https://github.com/oakestra/oakestra

ADD requirements.txt /

RUN pip install -r requirements.txt

ADD . /

ENV FL_ROOT_MANAGER_PORT=5073
EXPOSE 5073

CMD ["python", "fl_root_manager.py"]
