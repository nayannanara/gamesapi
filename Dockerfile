FROM python:3.11

ENV PYTHONUNBUFFERED 1

ENV PATH="/usr/local/bin:$PATH"

RUN pip install --upgrade pip

WORKDIR /games_api

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
