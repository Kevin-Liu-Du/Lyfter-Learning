class circle: #molde para crear objetos circulo 
    def __init__(self, radius): #metodo constructor para inicializar el radio del circulo
        self.radius = radius #atributo de instancia para almacenar el radio del circulo

    def get_area (self): #metodo para calcular el area del circulo
        return 3.14 * self.radius ** 2
    

# circle1 = circle(5)
# print(circle1.get_area())

# class rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def get_area(self):
#         return self.width * self.height
    
# rectangle1 = rectangle(4, 6)
# print(rectangle1.get_area())

# class square:
#     def __init__(self, side_length):
#         self.side_length = side_length
    
#     def get_area(self):
#         return self.side_length ** 2
    
# square1 = square(4)
# print(square1.get_area())
    
