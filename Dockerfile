FROM python:3.9.12-slim-buster AS base
WORKDIR /todo-app
RUN pip3 install poetry
COPY poetry.lock pyproject.toml wsgi.py ./
RUN poetry config virtualenvs.create false --local

FROM base AS production
RUN poetry install --no-dev
COPY todo_app ./todo_app
CMD poetry run gunicorn --bind 0.0.0.0:${PORT} "wsgi:start()" 

FROM base AS development
RUN poetry install
ENTRYPOINT [ "poetry", "run", "flask", "run", "--host=0.0.0.0"]

FROM base AS test
RUN poetry install
COPY ./todo_app ./todo_app
COPY ./tests ./tests
ENTRYPOINT [ "poetry", "run", "pytest" ]