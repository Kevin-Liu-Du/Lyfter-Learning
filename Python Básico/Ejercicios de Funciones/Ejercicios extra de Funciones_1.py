# Cree una función que reciba un texto y un carácter, y retorne cuántas veces aparece ese carácter en el texto
# "programacion"
# "Ingrese el carácter que desea buscar:" "o"
# "Se a encontrado 2 veces el carácter"

def count_character(word, character):
    character_counter = 0
    for character_word in word:
        if character_word == character:
            character_counter += 1
        
    return character_counter

word = input("Enter a random word: ")
character = input("Enter the character you want to search for: ")

print(f"The character has been found {count_character(word, character)} times.")