# Cree una función que reciba un string y retorne cuántas vocales contiene
# "Hola mundo"
# 4


def count_vocals(word):
    vocals = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    counter_vocals = 0
    for character in word:
        if character in vocals:
            counter_vocals += 1

    return counter_vocals





word = input("Ingrese una palabra: ")
print(count_vocals(word))