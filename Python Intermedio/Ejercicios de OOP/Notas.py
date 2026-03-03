# class Car:
# 	def __init__(self, model, year, color, top_speed):
# 		self.model = model
# 		self.year = year
# 		self.color = color
# 		self.top_speed = top_speed	
	
# 	def velocity(self, speed):
# 		if speed > self.top_speed:
# 			print("You are going too fast!")
# 		else:
# 			print("You are within the speed limit.")	
		


# my_car1 = Car("Toyota", 2020, "Red", 120)
# print(my_car1.model)  # Output: Toyota
# print(my_car1.year)   # Output: 2020
# print(my_car1.color)  # Output: Red
# print(my_car1.top_speed)  # Output: 120
# my_car1.velocity(130)  # Output: You are going too fast!

# class villager:
# 	def __init__(self, name, occupation):
# 		self.name = name
# 		self.occupation = occupation

# 	def talking(self):
# 		print(f"Hello, my name is {self.name} and I am a {self.occupation}.")

# # name_villager = input("Enter the name of the villager: ")
# # occupation_villager = input("Enter the occupation of the villager: ")
# # villager1 = villager(name_villager, occupation_villager)
# # villager1.talking()  # Output: Hello, my name is .... and I am a .....

# villager2 = villager("John", "Farmer")
# villager2.talking()  # Output: Hello, my name is John and I am a Farmer.

# villager3 = villager("Alice", "Blacksmith")
# villager3.talking()  # Output: Hello, my name is Alice and I am a Blacksmith.

# villager4 = villager("Bob", "Merchant")
# villager4.talking()  # Output: Hello, my name is Bob and I am a Merchant.

class Vehiculo:
	is_on: bool
	ruedas: int

	def encender(self):
		self.is_on = True
		print("Vehiculo encendida")

	def apagar(self):
		self.is_on = False

class Computadora:
	is_on: bool

	def encender(self):
		self.operative_system = "Windows"
		self.is_on = True
		print("Computadora encendida")

	def apagar(self):
		self.is_on = False

object_list = [
	Vehiculo(),
	Vehiculo(),
	Computadora(),
	Computadora(),
]

for object in object_list:
	object.encender()