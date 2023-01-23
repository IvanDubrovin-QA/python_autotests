import requests
import json
token = '62a37342da00f4660c8c6117bedb1c10'
response = requests.post('https://pokemonbattle.me:5000//pokemons', json = {
    "name": "Иванамберван",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"
},
 headers = {'Content-Type': 'application/json', 'trainer_token': token})
print(response.text)

pokemon_id = response.json()['id']

response_change = requests.put('https://pokemonbattle.me:5000/pokemons', json = {
    "pokemon_id": pokemon_id,
    "name": "Иваннамберван",
    "photo": ""
},
 headers = {'Content-Type': 'application/json', 'trainer_token': token})
print(response_change.text)

response_add = requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball', json = {
    "pokemon_id": pokemon_id
},
 headers = {'Content-Type': 'application/json', 'trainer_token': token})
print(response_add.text)
