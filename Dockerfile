FROM ubuntu:22.04

RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y python3.10 python3-pip && \
    pip install --upgrade pip

WORKDIR /app

COPY ./requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY ./StoreFront /app/StoreFront
COPY ./store /app/StoreFront
COPY ./playground /app/StoreFront
COPY ./likes /app/StoreFront
COPY ./tags /app/StoreFront
COPY ./manage.py /app/StoreFront
COPY ./.pgpass /app/StoreFront

CMD ["systemctl", "restart", "postgres"]