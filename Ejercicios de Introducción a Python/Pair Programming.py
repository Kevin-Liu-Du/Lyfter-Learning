#Dadas las horas trabajadas de una persona y su tarifa por hora, calcular y mostrar su salario.

horas_trabajadas = int(input("Ingrese sus horas trabajadas: "))
tarifa_por_hora = int(input("Ingrese su tarifa por hora: "))
salario = horas_trabajadas * tarifa_por_hora
f_string = f'Su Salario seria de {salario}'
print(f_string)

'''Dado el nombre y apellido de un empleado, y el dominio .com de una empresa, 
genere su email usando el formato <nombre>.<apellido>@<dominio_de_empresa>.com.'''

nombre = input("Digite su nombre: ")
apellido = input("Digite el primer apellido: ")
empresa = input("Digite el nombre de la empresa: ")
email = f"Su correo es: {nombre}.{apellido}@{empresa}.com"
print(email)