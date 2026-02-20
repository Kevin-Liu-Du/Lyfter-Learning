import json

def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8')as file:
        pokemon = json.load(file) #se usa json.load porque arriba ya tengo el archivo abierto
        return pokemon
    
#print(read_json_file("pokemon.json"))

def validation_number(message):
    while True:
        try:
            value = int(input(message))
            if value < 0:
                print("The value must be greater than 0.")
            else:
                return value
        except ValueError:
            print("You must enter a valid number.")

def ask_pokemon_type():
    ptype = input("Pokémon type (if there is more than one, separate them with commas ','): ")
    types_list = ptype.split(",")

    clean_types = []
    for t in types_list:
        clean_types.append(t.strip())

    return clean_types

def ask_for_data():
    name = input("Pokemon name: ")
    pokemon_type = ask_pokemon_type()

    level = validation_number("Pokemon Level: ")
    hp = validation_number("HP: ")
    attack = validation_number("Attack: ")
    defense = validation_number("Defense: ")
    sp_attack = validation_number("Sp. Attack: ")
    sp_defense = validation_number("Sp. Defense: ")
    speed = validation_number("Speed: ")

    new_pokemon = {
        "name": {
            "english": name
        },
        "level": level,
        "type": 
            pokemon_type,
        "base": {
            "HP": hp,
            "Attack": attack,
            "Defense": defense,
            "Sp. Attack": sp_attack,
            "Sp. Defense": sp_defense,
            "Speed": speed
        }
    }

    return new_pokemon



def add_pokemon_to_json(file_path):
    pokemon_list = read_json_file(file_path)
    new_pokemon = ask_for_data()
    pokemon_list.append(new_pokemon)
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(pokemon_list, file, indent=4)

add_pokemon_to_json("pokemon.json")
