import pytest
from todo_app.data.item import Item
from todo_app.view_models.index_page_view_model import IndexPageViewModel

todo_items = [
    Item('id_1', 'title_1', 'To Do'),
    Item('id_2', 'title_2', 'To Do')
]
doing_items = [
    Item('id_3', 'title_3', 'Doing'),
    Item('id_4', 'title_4', 'Doing')
]
done_items = [
    Item('id_5', 'title_5', 'Done'),
    Item('id_6', 'title_6', 'Done')
]

all_items = todo_items + doing_items + done_items


@pytest.fixture
def view_model():
    return IndexPageViewModel(all_items)


def test_view_model_todo_items(view_model: IndexPageViewModel):

    assert view_model.todo_items == todo_items


def test_view_model_doing_items(view_model: IndexPageViewModel):

    assert view_model.doing_items == doing_items


def test_view_model_done_items(view_model: IndexPageViewModel):

    assert view_model.done_items == done_items
