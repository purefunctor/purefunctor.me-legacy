FROM python:3.8-buster

WORKDIR /app
COPY . .

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIPENV_HIDE_EMOJIS=1 \
    PIPENV_IGNORE_VIRTUALENVS=1 \
    PIPENV_NOSPIN=1

RUN pip install --upgrade pip
RUN pip install --upgrade pipenv && pipenv install --system --deploy
