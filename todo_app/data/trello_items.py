import os
import requests

from todo_app.data.item import Item


def generate_params(params):
    key = os.getenv('TRELLO_SECRET_KEY')
    token = os.getenv('TRELLO_SECRET_TOKEN')
    authentication_params = {'key': key, 'token': token}
    return {**authentication_params, **params}


def get_trello_column_list_from_name(column_name):
    board_id = os.getenv('TRELLO_BOARD_ID')
    url = (f'https://api.trello.com/1/boards/{board_id}/lists')

    response = requests.get(
        url,
        params=generate_params({'cards': 'open',
                                'fields': 'name'})
    )

    for column_list in response.json():
        if column_list['name'] == column_name:
            return column_list

    raise Exception(
        f'Could not find column with name {column_name} in this board')


def get_items_from_column(column_name):
    column_list = get_trello_column_list_from_name(column_name)
    items = []
    for card in column_list['cards']:
        items.append(Item.from_trello_card(card, column_list))
    return items


def get_column_id(column_name):
    return get_trello_column_list_from_name(column_name)['id']


def add_item_to_column(item, column_name):
    column_id = get_column_id(column_name)

    url = 'https://api.trello.com/1/cards'

    requests.post(
        url,
        params=generate_params({'name': item,
                                'idList': column_id})
    )


def move_item_to_column(item_id, column_name):
    column_id = get_column_id(column_name)

    url = (f'https://api.trello.com/1/cards/{item_id}')

    requests.put(
        url,
        params=generate_params({'idList': column_id})
    )
