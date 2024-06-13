FROM python:3.12.3-slim

ENV PYTHIA_DIR=/opt/pythia

RUN mkdir -p ${PYTHIA_DIR}
WORKDIR ${PYTHIA_DIR}

COPY src/requirements.txt /tmp/requirements.txt

RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt
