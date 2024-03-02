FROM ubuntu:22.04

RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y python3.10 python3-pip && \
    pip install --upgrade pip

WORKDIR /StoreFront

COPY ./requirements.txt /StoreFront/
RUN pip install --no-cache-dir -r requirements.txt

COPY ./StoreFront /StoreFront/StoreFront
COPY ./store /StoreFront/store
COPY ./playground /StoreFront/playground
COPY ./likes /StoreFront/likes
COPY ./tags /StoreFront/tags
COPY ./manage.py /StoreFront/manage.py
COPY ./.pgpass /StoreFront/.pgpass
COPY ./.pg_service.conf /StoreFront/.pg_service.conf

ENV PGSERVICEFILE=/StoreFront/.pg_service.conf
ENV PYTHONUNBUFFERED 1
EXPOSE 5000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:5000"]