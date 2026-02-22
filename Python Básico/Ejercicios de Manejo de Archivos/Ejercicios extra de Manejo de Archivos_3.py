# Cree un programa que:
# Lea un archivo línea por línea
# Convierta cada línea a mayúsculas
# Escriba el contenido en un nuevo archivo
# Ejemplo:
# Entrada:
# archivo original:
# hola mundo
# esto es python
#Salida:
#HOLA MUNDO
#ESTO ES PYTHON

def open_file_read_line_by_line(file_name):
    with open(file_name) as file:
        line_word = file.readlines()
    return line_word

#open_file_read_line_by_line("Extra exercises on File Management_3.txt")

def convert_to_upper_case(file_path):
    word_list = open_file_read_line_by_line("Extra exercises on File Management_3.txt")
    with open(file_path, 'w', encoding='utf-8') as file:
        for line in word_list:
            upper_case_text = line.upper()
            file.write(upper_case_text)

convert_to_upper_case("Result Extra exercises on File Management_3")