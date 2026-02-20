# Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
# Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
# “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”

def sort_alphabetically(random_strings):
    separated = random_strings.split('-')#los separa por "-"
    #list_1 = []
    #list_1.append(separated)
    #print(separated)
    separated.sort() #los ordena alfabeticamente
    #print(separated)
    #for elements in separated:
    strings = "-".join(separated) #los unen y luego lo convierten en strings

    return strings



print(sort_alphabetically('python-variable-funcion-computadora-monitor'))