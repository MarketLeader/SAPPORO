FROM python:slim

WORKDIR /opt/SAPPORO/SAPPORO-web

RUN apt update && \
    apt install -y \
    build-essential \
    curl \
    iproute2 \
    jq \
    tree

COPY etc/requirements.txt /tmp

RUN pip install -U pip wheel setuptools && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /tmp/requirements.txt

COPY entry_point.sh /usr/local/bin
ADD https://raw.githubusercontent.com/eficode/wait-for/master/wait-for /usr/local/bin

COPY src /opt/SAPPORO/SAPPORO-web/src

CMD ["entry_point.sh"]
