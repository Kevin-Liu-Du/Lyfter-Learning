# Crea una función llamada sumar_lista(lista) que:
# Reciba una lista con valores mixtos (números y strings).
# Intente convertir cada elemento a float.
# Sume únicamente los valores válidos.
# Ignore los valores inválidos sin detener el programa.
# Usa try / except ValueError
# Retorna la suma total
# ['10', '5.5', 'manzana', '3', 'n/a']
# Resultado: 18.5


def convert_to_float(value):
    try:
        return float(value)
    except ValueError:
        return None


def sum_list(random_list):
    total = 0

    for element in random_list:
        number = convert_to_float(element)
        if number is not None:
            total += number

    return total



result = sum_list(['10', '5.5', 'manzana', '3', 'n/a'])
print(result)
