FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONPATH "${PYTHONPATH}:/PuckwheatBarser/backend"
RUN mkdir /app

WORKDIR /app

COPY backend/requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY backend /app/