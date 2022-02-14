from flask import Flask, render_template, redirect, request
from todo_app.data.trello_items import add_item_to_column, get_items_from_column, move_item_to_column
from todo_app.view_models.index_page_view_model import IndexPageViewModel


def createApp():

    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template(
            'index.html',
            model=IndexPageViewModel(
                todo_items=get_items_from_column('To Do'),
                doing_items=get_items_from_column('Doing'),
                done_items=get_items_from_column('Done')
            )
        )

    @app.route('/add', methods=['POST'])
    def addItemToTodo():
        add_item_to_column(request.form.get('title'), 'To Do')
        return redirect('/')

    @app.route('/complete_item/<id>', methods=['POST'])
    def completeItem(id):
        move_item_to_column(id, 'Done')
        return redirect('/')

    return app
