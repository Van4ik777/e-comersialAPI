FROM python:3.11-slim

RUN apt update && apt install -y libpq-dev gcc && python --version

COPY ./requirements.txt /app/requirements.txt
RUN python -m pip install --upgrade pip && pip install -r /app/requirements.txt

COPY ./src /app/src

WORKDIR /app/src

CMD ["bash", "../commands/start_server_dev.sh"]