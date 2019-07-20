FROM python:slim

WORKDIR /opt/SAPPORO/SAPPORO-service

RUN apt update && \
    apt install -y \
    build-essential

COPY requirements.txt /tmp

RUN pip install -U pip wheel setuptools && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /tmp/requirements.txt

# The workflow engine you want to use.
RUN apt install -y \
    cwltool && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

CMD ["tail", "-f", "/dev/null"]
