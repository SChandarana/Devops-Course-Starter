FROM python:3.9.12-slim-buster AS base
WORKDIR /todo-app
RUN pip3 install poetry
COPY poetry.lock pyproject.toml wsgi.py ./
RUN poetry install --no-dev
COPY todo_app ./todo_app
ENTRYPOINT [ "poetry", "run", "gunicorn", "--bind", "0.0.0.0:8080", "wsgi:start()" ]

