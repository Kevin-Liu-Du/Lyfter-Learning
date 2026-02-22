#Cree un programa que le pida al usuario ingresar 5 palabras. 
#Luego muestre una nueva lista con solo aquellas palabras que tengan más de 4 letras

word_list = []
new_list = []

for words in range(0, 5):
    words = input("Ingrese una palabra: ")
    word_list.append(words)

for filtered in word_list:
    if len(filtered) > 4:
        new_list.append(filtered)

print(new_list)
