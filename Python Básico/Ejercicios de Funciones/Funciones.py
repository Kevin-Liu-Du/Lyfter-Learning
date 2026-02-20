'''
def get_average_score(scores): #scores = juan_scores y juan_scores es un diccionario
    return (scores["spanish_score"] + scores["science_score"] + scores["history_score"]) / 3
# va a acceder a los valores de juan_scores, suma los 3 valores y luego lo divide para luego devolver el resultado
# juan_scores["average_score"] == lo que retorno

def is_student_exempted(scores):
    return scores["average_score"] > 70 #accede al diccionario scores["average scores"]
#compara el resultado que anteriormente habia retornado, y devuele un booleano


# Scores
students = [
    {
        "name": "Juan",
        "spanish_score": 75,
        "science_score": 56,
        "history_score": 54,
    },
    {
        "name" : "Sofia",
        "spanish_score": 64,
        "science_score": 56,
        "history_score": 98,
    },
    {
        "name": "Paul",
        "spanish_score": 72,
        "science_score": 75,
        "history_score": 79,
    }
]

for student in students:
    student["average_score"] = get_average_score(student)
    student["is_exempted"] = is_student_exempted(student)
    print(student["name"], " is_exempted is ", student["is_exempted"])



# Averages
juan_scores["average_score"] = get_average_score(juan_scores)
sofia_scores["average_score"] = get_average_score(sofia_scores)
paul_scores["average_score"] = get_average_score(paul_scores)

juan_scores["is_exempted"] = is_student_exempted(juan_scores)
sofia_scores["is_exempted"] = is_student_exempted(sofia_scores)
paul_scores["is_exempted"] = is_student_exempted(paul_scores)


variable_outside_function_scope = 7

def print_variable():
    print(f'Inside function: {variable_outside_function_scope}')


print_variable()
print(f'Outside function: {variable_outside_function_scope}')
'''



def remove_tenths(numbers_list):
    index = 0
    while (index < len(numbers_list)):
        if numbers_list[index] % 10 == 0:
            numbers_list.pop(index)
        else:
            index += 1


def multiply_numbers_by_2(numbers_list):
    for index, number in enumerate(numbers_list):
        numbers_list[index] = number * 2


def main():
    numbers_list = [53, 60, 32, 62, 400, 10]
    remove_tenths(numbers_list)
    multiply_numbers_by_2(numbers_list)
    print(numbers_list)


if __name__ == "__main__":
    main()