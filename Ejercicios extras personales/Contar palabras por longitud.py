#Contar palabras por longitud

words = ["sol", "luna", "estrella", "mar", "cielo"]

result = {}

for palabra in words:
    #print(words)
    length = len(palabra)
    if length not in result:
        result[length] = []

    result[length].append(palabra)

print(result)
