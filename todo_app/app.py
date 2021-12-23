from flask import Flask, render_template, redirect, request

import todo_app.data.session_items as session_items
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/')
def index():
    return render_template('index.html', items=session_items.get_items())

@app.route('/add', methods=['POST'])
def addItem():
    session_items.add_item(request.form.get('title'))
    return redirect('/')