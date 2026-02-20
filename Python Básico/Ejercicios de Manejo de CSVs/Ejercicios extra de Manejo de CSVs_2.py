import csv

def read_csv_file(file_path):
    game_list = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            game_list.append(row)

    return game_list
        
def ask_rating():
    rating_ESRB =("EC", "E", "E10+", "T", "M", "AO", "RP")
    while True:
        enter_rating = input("Enter a ESRB rating: ").upper()
        if enter_rating not in rating_ESRB:
            print("Error, not in the category")
        else:
            return enter_rating

# def show_result_rating_game():
#     rating_result = ask_rating()
#     game_list = read_csv_file("Game_list_with_coma.csv")
#     found_rating = False
#     for each_dictionary in game_list:
#         rating_dictionary = each_dictionary["Rating"]
#         if rating_result == rating_dictionary:
#             print(f"Games found: {each_dictionary}")
#             found_rating = True

#     if not found_rating:
#         print("No games with that rating have been found. ")


def show_result_rating_game():
    rating_result = ask_rating()
    game_list = read_csv_file("Game_list_with_coma.csv")
    result_list = []
    for each_dictionary in game_list:
        rating_dictionary = each_dictionary["Rating"]
        if rating_result == rating_dictionary:
            result_list.append(each_dictionary)
    
    if result_list == []:
        print("No games with that rating have been found. ")
    else:
        print(f"{len(result_list)} games have been found in the classification {rating_result}.")
        for each_dictionary in result_list:
            print(each_dictionary)


show_result_rating_game()