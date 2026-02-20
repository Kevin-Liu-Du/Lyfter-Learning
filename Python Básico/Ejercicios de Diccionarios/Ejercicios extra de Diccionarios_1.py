#Cree un diccionario que guarde el total de ventas de cada UPC

sales = [
	{ #Position 0
		'date': '27/02/23',
		'customer_email': 'joe@gmail.com',
		'items': [
			{
				'name': 'Lava Lamp',
				'upc': 'ITEM-453',
				'unit_price': 65.76,
			},
			{
				'name': 'Iron',
				'upc': 'ITEM-324',
				'unit_price': 32.45,
			},
			{
				'name': 'Basketball',
				'upc': 'ITEM-432',
				'unit_price': 12.54,
			},
		],
	},
	{ #Position 1
		'date': '27/02/23',
		'customer_email': 'david@gmail.com',
		'items': [
			{
				'name': 'Lava Lamp',
				'upc': 'ITEM-453',
				'unit_price': 65.76,
			},
			{
				'name': 'Key Holder',
				'upc': 'ITEM-23',
				'unit_price': 5.42,
			},
		],
	},
	{ #Position 3
		'date': '26/02/23',
		'customer_email': 'amanda@gmail.com',
		'items': [
			{
				'name': 'Key Holder',
				'upc': 'ITEM-23',
				'unit_price': 3.42,
			},
			{
				'name': 'Basketball',
				'upc': 'ITEM-432',
				'unit_price': 17.54,
			},
		],
	},
]

#print(sales[0]['items'][0]['name']) #lava lamp
#Recorri la lista y adentro hay 3 clientes en diccionario

result = {}

for sales_upc in sales:
    #print(sales_upc['items'])
    for item in sales_upc['items']:
        #print(item['upc'])
        #print(item['unit_price'])
        upc = item['upc']
        price = item['unit_price']
        if upc in result:
            result[upc] = result[upc] + price
        else:
            result[upc] = price    

print(result)

#es increible como de un enunciado tan grande que aveces hasta puede aparecerse abrumado y que la respuesta de codigo sea un pedacito muy peque;o,
#la logica que hay detras es una locura, puede que para algunas personas sea facil pero estuve casi 2h es solo este ejercicio, sin la ayuda de la IA yo sinceramente solo
#no lo pude haber hecho, no le pedi respuestas directa pero si pistas pero no es lo mismo que hacerlo uno solo sin ayuda que con pista entonces deja un sabor amargo en la boca
#es como que si no hubiera aprendido nada



