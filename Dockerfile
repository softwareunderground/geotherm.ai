FROM tiangolo/uvicorn-gunicorn:python3.7

LABEL maintainer="Software Underground"

COPY ./app /app

RUN pip install -r /app/requirements.txt
