# #no mutable
# def add_2_to_number(number):
#     number = number + 2

# my_integer = 5
# add_2_to_number(my_integer)

# print(my_integer)

# def add_2_to_number(number):
#     number = number + 2
#     return number

# my_integer = 5
# my_integer = add_2_to_number(my_integer)

# print(my_integer)

#mutable
# def add_2_to_list(my_list):
#     my_list.append(2)

# my_outside_list = [1, 3]
# add_2_to_list(my_outside_list)

# print(my_outside_list)

#no mutable
# def change_boolean_to_true(boolean):
#     boolean = True

# my_other_boolean = False
# change_boolean_to_true(my_other_boolean)

# print(my_other_boolean)

# my_string = "Hola" 
# my_string = my_string + "Mundo" 

my_string = "Hola"
print(id(my_string))

my_string = my_string + "Mundo"
print(id(my_string))
