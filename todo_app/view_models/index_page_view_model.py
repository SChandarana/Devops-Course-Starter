class IndexPageViewModel:
    def __init__(self, items) -> None:
        self._all_items = items

    @property
    def todo_items(self):
        return [item for item in self._all_items if item.status == 'To Do']

    @property
    def doing_items(self):
        return [item for item in self._all_items if item.status == 'Doing']

    @property
    def done_items(self):
        return [item for item in self._all_items if item.status == 'Done']
