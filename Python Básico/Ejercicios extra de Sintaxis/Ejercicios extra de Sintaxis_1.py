#Cree un pseudocódigo que le pida un precio de producto al usuario, calcule su descuento y muestre el precio final tomando en cuenta que:
#Si el precio es menor a 100, el descuento es del 2%.
#Si el precio es mayor o igual a 100, el descuento es del 10%.

price = int(input("Ingres el precio del producto: "))
if (price < 100):
    discount = price * 0.02
else:
    discount = price * 0.10

final_price = price - discount
print(f"El precio fianl del producto con descuento es de {final_price} $.")