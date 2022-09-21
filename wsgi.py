from todo_app.app import create_app
from dotenv import load_dotenv


def start():
    load_dotenv()
    return create_app()
