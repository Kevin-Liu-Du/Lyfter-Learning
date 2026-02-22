# Cree una función convertir_a_entero(lista) que:
# Reciba una lista de strings
# Intente convertir cada elemento a entero usando int()
# Use try-except para atrapar los errores ValueError
# Si algún elemento no puede convertirse, mostrar "No se pudo convertir el elemento: <valor>" y continuar con los demás
# entrada: my_list = ['4', 'hola', '10', '5.2']
# "Resultado:"
# "4" "convertido a" 4
# "No se pudo convertir el elemento: hola"
# "10" "convertido a" 10
# "No se pudo convertir el elemento: 5.2"

def convert_to_int(random_list):
    for each_element in random_list:
        conversion = each_element
        try:
            if not conversion.isdigit():
                raise ValueError()
            else:
                print(f"{each_element} converted to {conversion}")
        except ValueError as ex:
            print(f"The element could not be converted: {each_element}")

convert_to_int(['4', 'hola', '10', '5.2'])