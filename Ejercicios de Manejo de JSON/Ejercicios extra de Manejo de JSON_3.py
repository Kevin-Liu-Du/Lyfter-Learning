import json

def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8')as file:
        pokemon = json.load(file)
        return pokemon
    
#print(read_json_file("pokemon.json"))

def grouped_type():
    pokemon_list = read_json_file("pokemon.json")
    grouped = {}
    for each_pokemon in pokemon_list:
        pokemon_type = each_pokemon["type"]
        pokemon_name = each_pokemon["level"]
        for each_element in pokemon_type:
            if each_element not in grouped:
                grouped[each_element] = []

            grouped[each_element].append(pokemon_name)

    return grouped

#print(grouped_type())

def calculate_average():
    grouped_dictionary = grouped_type()
    for each_element, value in grouped_dictionary.items():
        average = round(sum(value)/len(value), 1) #el 1 es para solo un decimal
        print(f"Type: {each_element} -> Average of level: {average}")

calculate_average()