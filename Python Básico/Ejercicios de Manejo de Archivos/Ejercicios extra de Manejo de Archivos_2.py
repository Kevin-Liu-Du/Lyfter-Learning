# Cree un programa que abra un archivo de texto y cuente cuántas palabras contiene en total.
# (Considere que las palabras están separadas por espacios y/o saltos de línea)

def open_file(path):
    with open(path) as file:
        word_list = file.readlines()
    return word_list

#open_file("penguins.txt")    

def count_word():
    text_file = open_file("Extra exercises on File Management_2.txt")
    counter = 0
    for word in text_file:
        first_list = word.split() #por defecto toma en cuenta los espacios y saltos de linea
        amount = len(first_list)
        counter = counter + amount
    
    return counter


print(f"Este archivo contiene {count_word()} palabras")