FROM alpine:3.13
LABEL maintainer="Lorenzo Carnevale"
LABEL email="lcarnevale@unime.it"

ARG PORT=5000
ENV PORT=$PORT

COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app

RUN apk update && \
    apk add python3 python3-dev py3-pip && \
    pip3 install --upgrade pip && \
    pip3 install -r requirements.txt && \
    rm -rf /var/cache/apk/* \
    rm -rf /tmp/*
RUN mkdir -p /var/log/fileserver

EXPOSE 8000

COPY app /opt/app

CMD ["sh", "-c", "python3 main.py -v -p $PORT"]