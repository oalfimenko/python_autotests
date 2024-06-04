import requests

TOKEN = 'f7c6555d7932c25d3120e0f9eb3247a8'
URL = 'https://api.pokemonbattle.ru/v2'
HEADER = {
    'Content-Type' : 'application/json',
    'trainer_token' : TOKEN
}

ID = 4330 

body_create = {
    "name": "generate",
    "photo": "generate"
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.json())

pokemon_id = response_create.json()['id']

body_put = {
    "pokemon_id": pokemon_id,
    "name": "generate",
    "photo": "generate"
}

body_catch = {
    "pokemon_id": pokemon_id
}

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.json())

response_put = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_put)
print(response_put.json())


