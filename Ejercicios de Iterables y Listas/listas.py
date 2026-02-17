milky_way_planets = [
	'Mercury',
	'Venus',
	'Earth',
	'Mars',
	'Pluto',
	'Jupiter',
	'Saturn',
	'Uranus',
	'Neptune',
]

pluto_index = 0
for index, planet in enumerate(milky_way_planets):
    if planet == "Pluto":
        print(index) #aca te da la posicion de Pluto
        pluto_index = index

deleted_item = milky_way_planets.pop(pluto_index)
print(milky_way_planets)
print(f'Deleted item: {deleted_item}')
