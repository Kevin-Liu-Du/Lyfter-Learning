import csv

def read_csv_file(file_path):
    game_list = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            game_list.append(row)

    return game_list

def count_same_genre_games():
    game_list = read_csv_file("Game_list_with_coma.csv")
    result = {}
    for each_dictionary in game_list:
        genre = each_dictionary["Genre"]
        if genre not in result:
            result[genre] = 1
        else:
            result[genre] += 1

    return result

# def print_in_order():
#     count_result = count_same_genre_games()
#     for genre, count in count_result.items():
#         print(f"{genre}: {count}")

def print_in_order():
    count_result = count_same_genre_games()
    for genre, count in sorted(count_result.items()):
        print(f"{genre}: {count}")

print_in_order()