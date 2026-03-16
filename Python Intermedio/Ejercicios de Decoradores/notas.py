#Decoradores que hagan cosas despues de la función

def print_goodbye(func):
    def  wrapper():
        func()

    return wrapper

@print_goodbye
def function():
    print("Hello World")


function()#output Hello World

#-------------------------------------------------------------------------------------------------------------------------------

def print_goodbye(func):
    def  wrapper():
        func()
        print("Goodbye")#logica despues de la funcion

    return wrapper

@print_goodbye
def function():
    print("Hello World")


function()
#output Hello World
#Goodbye

#-------------------------------------------------------------------------------------------------------------------------------

def print_goodbye(func):
    def  wrapper():
        print("This is pre-function run")#logica antes de la funcion
        func()
        print("Goodbye")#logica despues de la funcion

    return wrapper

@print_goodbye
def function():
    print("Hello World")


function()
#This is pre-function run
#Hello World
#Goodbye

#-------------------------------------------------------------------------------------------------------------------------------
def print_goodbye(func):
    def  wrapper():
        print("This is pre-function run")
        func()
        print("Goodbye")#logica despues de la funcion

    return wrapper

@print_goodbye
def function():
    print("Hello World")

@print_goodbye
def big_function():
    print("Hello World")
    print("Hello World")
    print("Hello World")
    print("Hello World")
    print("Hello World")
    print("Hello World")
    


function()
#output Hello World
#Goodbye

big_function()
#out put:
#This is pre-function run
#Hello World
# Hello World
# Hello World
# Hello World
# Hello World
# Hello World
#Goodbye