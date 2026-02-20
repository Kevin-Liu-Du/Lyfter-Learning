def ask_game_amount():
    while True:
        try:
            amount = int(input("Enter the number of video games you want to save: "))
            if amount < 0:
                print("You must enter a number greater than 0.")
            else:
                return amount
        except ValueError:
            print("Error, only whole numbers are accepted.")


def ask_question():
    amount = ask_game_amount()
    counter = 0
    result = []
    while amount > counter:
        dictionary = {}
        name = input("Enter the name of the game:")
        dictionary["Name"] = name

        genre = input("Enter the game genre:")
        dictionary["Genre"] = genre

        developer = input("Enter the game development company:")
        dictionary["Developer"] = developer

        rating = input("Enter the game's ESRB rating:")
        dictionary["Rating"] = rating

        counter += 1
    
        result.append(dictionary)
    
    return result


game_headers = (
    "Name",
    "Genre",
    "Developer",
    "Rating",
)

import csv

def write_CSV_file(file_path, data, headers):
    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, headers, )
        writer.writeheader()
        writer.writerows(data)

write_CSV_file("Game_list_with_coma.csv",ask_question(), game_headers)

