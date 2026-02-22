def menu():
    menu = [
        "1. Suma",
        "2. Resta",
        "3. Multiplicación",
        "4. División",
        "5. Resultado",
        "6. Borrar resultado",
        "7. Salir"
    ]

    for each_option in menu:
        print(each_option)


while True:
    try:
        first_number = float(input("Ingrese un numero: ")) #se debe de aceptar int como float, string no deben de aceptar
        break
    except ValueError:
        print("Error, solo se aceptan valores negativos, positivos, y decimales.")


print("Que deseas hacer con el numero: ")
menu()

numero_actual = first_number #variable de estado el first number solo se usa una vez, 

options = 0  #sirve para arrancar el while
while options != 7: #si selecciono un 8 el menu continua, try, except??
    try:
        options = int(input("Seleccione una opción: "))
    except ValueError:
            print("Error, debe ingresar un numero valido.")
            continue
    if 1 <= options <= 4:
        try:
            second_number = float(input("ingrese otro numero: "))
        except ValueError:
            print("Error, debe ingresar un numero valido.")
            continue #esto lo que hace es volver a inciar el while, es decir va a mostrar el menu de nuevo

        if options == 4:
            if second_number == 0:
                print("Numero no valido, no se puede dividir entre 0, ingrese otro numero: ")
                continue

        if options == 1:
            result = numero_actual + second_number
            numero_actual = result
        elif options == 2:
            result = numero_actual - second_number
            numero_actual = result
        elif options == 3:
            result = numero_actual * second_number
            numero_actual = result
        elif options == 4:
            result = numero_actual / second_number
            numero_actual = result



    elif options == 5:
        print(numero_actual)
    elif options == 6:
        numero_actual = 0
        print(f"Resultado borrado. Valor Actual: {numero_actual}")
    elif options == 7:
        exit()
    else:
        print(("Numero no corresponde al menu."))




#el primer pensamiento que tuve es el fuljo completo como tal, de lo mas sencillo lo cual es una calculadora tiene que hacer lo basico y mostrar un resultado
#en el segundo intento, trate de meter mas funciones, haciendolo lo mas similar a una calculadora real, 
#creo que desde un principio no lo pense tan bien ya que al pensar de una vez en el flujo solo me concentre en lo general, y no lo especifico
#lo que tuve que haber hecho es ir de bloque en bloque o tal vez no?

