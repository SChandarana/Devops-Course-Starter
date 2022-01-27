from flask import Flask, render_template, redirect, request
from todo_app.data.trello_items import get_items_from_column, add_item_to_column, move_item_to_column

app = Flask(__name__)


@app.route('/')
def index():
    return render_template(
        'index.html',
        todo_items=get_items_from_column('To Do'),
        done_items=get_items_from_column('Done')
    )


@app.route('/add', methods=['POST'])
def addItemToTodo():
    add_item_to_column(request.form.get('title'), 'To Do')
    return redirect('/')


@app.route('/complete_item/<id>', methods=['POST'])
def completeItem(id):
    move_item_to_column(id, 'Done')
    return redirect('/')
