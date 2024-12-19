import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '5e0377cba9a4f4ed2b8d5dc6b87cf925'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '12556'
def test_status_code():
    responce = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID} )
    assert responce.status_code == 200

def test_trainer_name():
    responce = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID} )  
    assert responce.json()['data'][0]['trainer_name'] == 'Carter'