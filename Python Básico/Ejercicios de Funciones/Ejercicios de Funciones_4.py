# Cree una función que le de la vuelta a un string y lo retorne.
# Esto ya lo hicimos en iterables.
# “Hola mundo” → “odnum aloH”

def reversed_string(random_string):

    reversed_text = ""

    for index in range(len(random_string) -1, -1, -1):
        reversed_text = reversed_text + random_string[index]

    return reversed_text

print(reversed_string('Hola Mundo'))