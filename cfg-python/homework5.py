# 1. PIP is a package manager used to install libraries that other people have written


# 3.

#This will retrieve information about the pokemon

url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)

response = requests.get(url)
pokemon = response.json()

print(pokemon['name'])

#This will write it to the file
pokemon = input("Input a new item")

with open('pokemonlist.txt', 'r') as file:
    pokemon_list = file.read()

new_pokemon = pokemon_list + "\n" #+ #add here name of new pokemon list

with open('pokemonlist.txt', 'w+') as file:
    file.write(new_pokemon)
