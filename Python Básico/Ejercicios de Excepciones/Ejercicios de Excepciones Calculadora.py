
first_number = int(input("Ingres un numero: "))

menu = [
    "1. Suma",
    "2. Resta",
    "3. Multiplicación",
    "4. División",
    "5. Borrar resultado"
]

for options in menu:
    print(options)

select_options = int(input("Seleccione una operación:"))

second_number = int(input("Ingrese otro numero:"))


result = 0

if select_options == 1:
    result = first_number + second_number
elif select_options == 2:
    result = first_number - second_number
elif select_options == 3:
    result = first_number * second_number
elif select_options == 4:
    result = first_number / second_number
elif select_options == 5:
    exit()

print(f"El resultado de la operacion es de {result}")