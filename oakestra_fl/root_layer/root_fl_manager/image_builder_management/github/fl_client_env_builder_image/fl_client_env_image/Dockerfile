FROM docker.io/continuumio/miniconda3:24.1.2-0
LABEL org.opencontainers.image.source https://github.com/oakestra/oakestra

COPY . /

# COPY /cloned_repo/conda.yaml .
# RUN conda env update --file ./conda.yaml &&\
#     # https://flower.dev/docs/framework/how-to-install-flower.html
#     conda config --add channels conda-forge &&\
#     conda config --set channel_priority strict &&\
#     conda install mlflow flwr &&\
#     conda clean -tipy
# SHELL ["conda", "run", "-n", "base", "/bin/bash", "-c"]

# # Not sure if this is the best way
# COPY /cloned_repo/* .
# RUN mv client.py custom_client.py
# COPY oak_ml_client.py .

# # https://flower.dev/docs/framework/ref-telemetry.html
# ENV FLWR_TELEMETRY_ENABLED=0

