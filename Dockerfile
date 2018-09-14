FROM python:3.6-alpine

RUN adduser -D order-counter

WORKDIR /home/order-counter

RUN apk update && \
 apk add postgresql-libs && \
 apk add --virtual .build-deps gcc musl-dev postgresql-dev

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY migrations migrations
COPY order_counter.py boot.sh ./
COPY config.py.sample ./config.py
RUN chmod +x boot.sh

ENV FLASK_APP order_counter.py

RUN chown -R order-counter:order-counter ./
USER order-counter

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]