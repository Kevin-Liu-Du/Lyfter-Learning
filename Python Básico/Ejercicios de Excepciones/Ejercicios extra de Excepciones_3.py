# Cree una función sumar_valores(lista) que:
# Reciba una lista de elementos (strings, enteros, flotantes mezclados)
# Intente convertir cada elemento a tipo float
# Si puede, sume el valor y muestre: "<valor> sumado correctamente"
# Si no puede, muestre: "Elemento inválido: <valor>"
# Al final, imprima la suma total
# Ejemplo: my_list = ['10', 'manzana', '5.5', '3', 'n/a']
# 10.0 "sumado correctamente"
# "Elemento inválido: manzana"
# 5.5 "sumado correctamente"
# 3.0 "sumado correctamente"
# "Elemento inválido: n/a"
# "Total de la suma:" 18.5

# def sum_value(random_list):
#     result = 0
#     for each_elements in random_list:
#         #conversion_float = float(each_elements)
#         try:
#             conversion_float = float(each_elements)
#             if conversion_float != float(each_elements): #esto no tiene sentido
#                 raise ValueError
#             else:
#                 result = result + conversion_float
#                 print(f"{conversion_float} Sumado Correctamente")
#         except ValueError as ex:
#             print(f"Elemento invalido: {conversion_float}")

#     return result

# print(sum_value(['10', 'manzana', '5.5', '3', 'n/a']))

def sum_value(random_list):
    result = 0
    for each_elements in random_list:
        try:
            conversion_float = float(each_elements)
            result = result + conversion_float
            print(f"{conversion_float} Summed Correctly.")
            
        except ValueError as ex:
            print(f"invalid element: {each_elements}")

    return result

print(sum_value(['10', 'manzana', '5.5', '3', 'n/a']))