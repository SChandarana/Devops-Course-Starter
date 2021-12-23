import os
import requests
from requests.api import request

from todo_app.data.item import Item

key = os.getenv('TRELLO_SECRET_KEY')
token = os.getenv('TRELLO_SECRET_TOKEN')
board_id = os.getenv('TRELLO_BOARD_ID')

def convert_column_list_into_items(column_list):
    items = []
    for card in column_list['cards']:
        items.append(Item.from_trello_card(card, column_list))
    return items

def get_items_from_column(column_name):
    url = (f'https://api.trello.com/1/boards/{board_id}/lists')

    response = requests.request(
        'GET',
        url,
        params={
            'key': key,
            'token': token,
            'cards': 'open',
            'fields': 'name'
        }
    )

    for column_list in response.json():
        print(column_list)
        if column_list['name'] == column_name:
            return convert_column_list_into_items(column_list)

    raise Exception(f'Could not find column with name {column_name} in this board')

def get_column_id(column_name):
    url = (f'https://api.trello.com/1/boards/{board_id}/lists')

    response = requests.request(
        'GET',
        url,
        params={
            'key': key,
            'token': token,
            'cards': 'open',
            'fields': 'name'
        }
    )

    for column_list in response.json():
        if column_list['name'] == column_name:
            return column_list['id']
    
    raise Exception(f'Could not find column with name {column_name} in this board')

def add_item_to_column(item, column_name):
    column_id = get_column_id(column_name)

    url = 'https://api.trello.com/1/cards'

    requests.request(
        'POST',
        url,
        params= {
            'key': key,
            'token': token,
            'name': item, 
            'idList': column_id
        }
    )

def move_item_to_column(item_id, column_name):
    column_id = get_column_id(column_name)

    url = (f'https://api.trello.com/1/cards/{item_id}')

    requests.request(
        'PUT',
        url,
        params= {
            'key': key,
            'token': token,
            'idList': column_id
        }
    )

