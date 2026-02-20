#Agrupar empleados por departamento
#Dada una lista de empleados donde cada uno tiene nombre, correo y departamento, cree un diccionario que agrupe los empleados por su departamento:
employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]

result = {} #Voy a usar este diccionario para agrupar empleados por departamento

for people in employees: #Voy a recorrer la lista employees, uno por uno. "people" representa un solo empleado
    department = people["department"] #Saca el departamento del empleado actual
    print(department) 
    if department not in result: #Ya existe este departamento como clave en el diccionario result
        result[department] = [] #Esto pasa solo si ese departamento no existe en diccionario result 
                                #Crea una nueva entrada en el diccionario con este departamento y asígnale una lista vacía

    result[department].append(people) #Agrega el empleado actual (people) a la lista del departamento correspondiente

print(result)








#department = {
#    "ventas" : [
#        {
#            "name" : "Carlos",
#            "email": "carlos@empresa.com",
#        },
#        {
#            "name": "Luis",
#            "email": "luis@empresa.com",
#        }
#    ],
#}