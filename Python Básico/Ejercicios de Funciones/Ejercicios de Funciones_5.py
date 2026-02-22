# Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
# “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”

def count_upper_and_lower_case(random_strings):
    upper_case = 0
    lower_case = 0
    for letters in random_strings:
        if letters.isupper() == True:
            upper_case += 1
        elif letters.islower() == True:
            lower_case += 1


    print(f"There’s {upper_case} upper cases and {lower_case} lower cases")


count_upper_and_lower_case("I love Nación Sushi")


# def count_upper_and_lower_case(random_strings):
#     upper_case = 0
#     lower_case = 0
#     for letters in random_strings:
#         if letters.isupper() == True:
#             upper_case += 1
#         elif letters.islower() == True:
#             lower_case += 1

#     return upper_case, lower_case

#     #print(f"There’s {upper_case} upper cases and {lower_case} lower cases")


# print(count_upper_and_lower_case("I love Nación Sushi"))

