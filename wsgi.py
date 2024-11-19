from todo_app.app import create_app
from dotenv import load_dotenv
# comment for CI

def start():
    load_dotenv()
    return create_app()
