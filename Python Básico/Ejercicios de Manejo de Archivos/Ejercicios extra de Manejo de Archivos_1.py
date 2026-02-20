#Cree un programa que lea un archivo con texto línea por línea, quite los saltos de línea (\n) y escriba todo el contenido en un solo renglón en un nuevo archivo

def open_file_per_line(path):
    with open(path) as file:
        line_to_list = file.readlines() #read lee el archivo tal cual, #readlines() te lo convierte en una lista
        return line_to_list
    
def delete_empty_spaces():
    first_list = open_file_per_line("Extra exercises on File Management_1.txt")
    clean_list = []
    for each_element in first_list:
        clean_element = each_element.strip()
        clean_list.append(clean_element)
    return clean_list

def write_single_line(file_path):
    second_list = delete_empty_spaces()
    with open(file_path, 'w', encoding='utf-8') as file:
        for word in second_list:
            file.write(word + " ")


write_single_line("Single Line")
