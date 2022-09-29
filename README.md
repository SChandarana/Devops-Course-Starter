# DevOps Apprenticeship: Project Exercise

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. You will need to populate the values in this with your own api keys/secrets 

## Trello

To use this app, a Trello account is required. This can be made for free on the [Trello Website](https://trello.com/). And then follow [these instructions](https://trello.com/app-key/) for obtaining an API key and token for the `.env` file. 

You will also need to create a board with 3 columns: `'To Do'`, `'Doing'` and `'Done'`

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Running the tests

This project uses pytest. To run all the tests use:

```bash
$ poetry run pytest tests
```

## Ansible

If changing or adding new files for ansible you will want to load them into the control node by running the following in the root of this project.

```bash
$ sh ansible/copy_to_vm.sh
```

This will copy all files from `ansible/vm_files/` into `/home/ec2-user` on the control node

To run the playbook, ssh into the control node and run

```bash
$ ansible-playbook vm_files/playbook.yml -i vm_files/inventory
```

## Docker

To run the app using docker, you can do the following:

First, build the dev and prod docker images:

For the dev image run:
```bash
$ docker build --target production --tag todo-app:dev .
```

For the prod image run:
```bash
$ docker build --target production --tag todo-app:prod .
```

Then you can run the app:

To run in dev mode:
```bash
$ docker run --env-file ./.env -p 5100:5000 --mount type=bind,source=$(pwd)/todo_app,target=/todo-app/todo_app todo-app:dev
```
You can then visit [`http://localhost:5100/`](http://localhost:5100/) to see the dev app

To run in prod mode:
```bash
$ docker run --env-file ./.env -p 8080:80 --mount type=bind,source=(pwd)/todo_app,target=/todo-app/todo_app todo-app:prod
```
You can then visit [`http://localhost:8080/`](http://localhost:8080/) to see the prod app

N.B. If you are using the fish terminal then you will need to omit the `$`

