# Experimente con el concepto de scope:
# Intente accesar a una variable definida dentro de una función desde afuera.
# Intente accesar a una variable global desde una función y cambiar su valor.

# def variable_inside():
#     hello = 9
#     print(f"Inside varibale:{hello}")

# variable_inside()
# print(f"Outside variable: {hello}")

outside_variable = 10
def access_outside(num1):
    operation = outside_variable + num1
    print(operation)

access_outside(9)
