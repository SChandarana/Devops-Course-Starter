from todo_app.data.trello_items import get_items_from_column


class IndexPageViewModel:
    def __init__(self) -> None:
        self._todo_items = get_items_from_column('To Do')
        self._doing_items = get_items_from_column('Doing')
        self._done_items = get_items_from_column('Done')

    @property
    def todo_items(self):
        return self._todo_items

    @property
    def doing_items(self):
        return self._doing_items

    @property
    def done_items(self):
        return self._done_items

