import csv

def read_csv_file(file_path):
    game_list = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            game_list.append(row)

    return game_list

def ask_developer():
    developer = input("Enter a developer: ").strip().upper()
    return developer

def compare():
    game_list = read_csv_file("Game_list_with_coma.csv")
    user_developer = ask_developer()
    result = []
    for each_dictionary in game_list:
        developer = each_dictionary["Developer"].strip().upper()
        if developer == user_developer:
            result.append(each_dictionary)

    return result, user_developer

def print_readable_format():
    game_list, user_developer = compare()
    if game_list == []:
        print("No games related to that developer have been found.")
    else:
        print(f"Video games developed by {user_developer}: ")
        for games in game_list:
            print(
                f"Game: {games["Name"]},"
                f" Rating: {games["Rating"]}, Genre: {games["Genre"]}" 
            )

print_readable_format()