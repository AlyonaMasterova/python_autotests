import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '5e0377cba9a4f4ed2b8d5dc6b87cf925'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
body_create = {
    "name": "Бублик",
    "photo_id": 50
}
body_change = {
    "pokemon_id": "162306",
    "name": "Кексик",
    "photo_id": 2
}
body_add = {
    "pokemon_id": "162306"
}

# Создать покемона
'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''


# Сменить имя покемона
'''response_create = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_create.text)'''

# Поймать в покебол
response_create = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add)
print(response_create.text)




