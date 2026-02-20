# Cree un programa que:
# Pida al usuario una línea de texto
# Agregue esa línea al final de un archivo existente
# Si el archivo no existe, lo crea automáticamente
# Ejemplo:
# entrada:
# "Este es un nuevo registro"
# salida:
# "El texto se agrega al final del archivo sin borrar lo anterior"

def ask_for_string():
    string = input("enter a random sentence: ")
    return string

def add_to_file(file_path):
    string = ask_for_string()
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(string + "\n")

add_to_file("Extra exercises on File Management_4.txt")