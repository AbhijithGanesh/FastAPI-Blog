FROM python:3.9

LABEL FastAPI Blog

ENV PYTHONUNBUFFERED 1

COPY requirements/dev.txt requirements.txt

RUN pip install -r requirements.txt


WORKDIR /app/BlogSite
COPY /app /app

EXPOSE 8080