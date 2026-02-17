import csv

def read_csv_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter='\t')
        for row in reader:
            for each_element in row:
                print(f"{each_element}: {row[each_element]}")

read_csv_file('Game_list_with_tabulation.csv')

import csv

def read_csv_file(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            for each_element in row:
                print(f"{each_element}: {row[each_element]}")

read_csv_file('Game_list_with_coma.csv')