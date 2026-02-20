import json

def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8')as file:
        pokemon = json.load(file)
        return pokemon
    
#print(read_json_file("pokemon.json"))

def show_statistics():
    pokemon_list = read_json_file("pokemon.json")
    for each_pokemon in pokemon_list:
        name = each_pokemon["name"]["english"]
        attack = each_pokemon["base"]["Attack"]
        defense = each_pokemon["base"]["Defense"]
        speed = each_pokemon["base"]["Speed"]

        print(f"Name: {name}\nAttack: {attack}\nDefense: {defense}\nSpeed: {speed}\n")

show_statistics()

def show_statistics_upgrade():
    pokemon_list = read_json_file("pokemon.json")
    for each_pokemon in pokemon_list:
        name = each_pokemon["name"]["english"]
        print(f"Name: {name}")
        base_stats = each_pokemon["base"]
        for stats, value in base_stats.items():
            print(f"{stats}: {value}")
        print()

show_statistics_upgrade()

def show_statistics_upgrade_2():
    pokemon_list = read_json_file("pokemon.json")
    for each_pokemon in pokemon_list:
        name = each_pokemon["name"]["english"]
        print(f"Name: {name}")
        base_stats = each_pokemon["base"]
        for stats, value in base_stats.items():
            if stats == "Attack":
                print(f"{stats}: {value}")
            if stats == "Defense":
                print(f"{stats}: {value}")
            if stats == "Speed":
                print(f"{stats}: {value}")
        print()

show_statistics_upgrade_2()
