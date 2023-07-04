FROM python:3.11-slim

WORKDIR /games_api

COPY requirements.txt /games_api/

RUN pip install --upgrade pip && \
    pip install poetry && \
    useradd -m core && \
    chown -R games_api.games_api /games_api && \
    cd /games_api && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi

USER games_api

ADD . /games_api/
