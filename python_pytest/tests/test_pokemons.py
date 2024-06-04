import requests
import pytest

TOKEN = 'f7c6555d7932c25d3120e0f9eb3247a8'
URL = 'https://api.pokemonbattle.ru/v2'
HEADER = {
    'Content-Type' : 'application/json',
    'trainer_token' : TOKEN
}

ID = '4330' 

def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200

def test_check_trainer():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : ID})
    assert response.json()['data'][0]['trainer_name'] == 'afloy'
