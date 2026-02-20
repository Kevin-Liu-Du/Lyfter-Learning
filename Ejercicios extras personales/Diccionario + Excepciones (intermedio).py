
def average_notes(students):
    result = {}
    for each_student in students:
        counter = 0
        total_sum = 0
        
        notes = students[each_student]
        for each_notes in notes:
            try:
                converted = float(each_notes)
                total_sum += converted
                counter += 1
            except ValueError:
                None


        if counter == 0:
            result[each_student] = "No result"
        else:
            average = total_sum / counter
            result[each_student] = average

    return result

dictionary = {
    "Ana": [90, 85, 88],
    "Luis": [70, "Eighty", 75],
    "Andrea": []
}

print(average_notes(dictionary))