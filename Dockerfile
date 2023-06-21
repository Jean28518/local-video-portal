FROM python:3.11-alpine

RUN apk add gettext

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./videoportal /app

WORKDIR /app
VOLUME ./sqlite-data:/app/db

COPY ./entrypoint.sh /
ENTRYPOINT [ "sh", "/entrypoint.sh" ]