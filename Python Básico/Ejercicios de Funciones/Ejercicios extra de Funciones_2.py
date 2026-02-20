# Cree una función que reciba una lista de palabras y un número n, y retorne una nueva lista con solo las palabras que tengan más de n letras
# ["cielo", "sol", "maravilloso", "día"]
# "Ingrese el numero de letras minimas en la palabra: " 4
# ["cielo", "maravilloso"]

def sort_words(random_list, number):
    result_list = []
    for word in random_list:
        if len(word) > number:
            result_list.append(word)

    return result_list

print(sort_words(["cielo", "sol", "maravilloso", "día"], 4))



# def sort_words(random_list, number_character):
#     result_list = []
#     for word in random_list:
#         if len(word) > number_character:
#             result_list.append(word)

#     return result_list

# def data():
#     number_of_words = int(input("Ingrese la cantidad de palabras que quieres: "))
#     counter = 0
#     random_list = []
#     while counter < number_of_words:
#         random_list_words = input("Ingrese una palabra random: ")
#         random_list.append(random_list_words)
#         counter += 1

#     number_character = int(input("Ingrese el numero de letras minimas en la palabra: "))

#     return random_list, number_character

# random_list, number_character = data()
# result = sort_words(random_list, number_character)
# print(result)
