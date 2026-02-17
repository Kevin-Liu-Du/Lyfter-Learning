import json

def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8')as file:
        pokemon = json.load(file)
        return pokemon
    
#print(read_json_file("pokemon.json"))

def ask_for_pokemon():
    question = input("Enter the type of Pokémon you want to search for: ").strip().capitalize()
    return question

def print_result():
    user_type = ask_for_pokemon()
    pokemon_list = read_json_file("pokemon.json")
    result_list = []
    for each_pokemon in pokemon_list:
        pokemon_type = each_pokemon['type'] #this is a list
        if user_type in pokemon_type:
                pokemon_name = each_pokemon["name"]["english"]
                result_list.append(pokemon_name)
    
    return result_list

def validation():
    name_list = print_result()
    if name_list == []:
        print("There is no Pokémon with that element.")
    else:
        print("The Pokémon that exist of that type are: ")
        for each_pokemon in name_list:
            print(each_pokemon)

validation()
