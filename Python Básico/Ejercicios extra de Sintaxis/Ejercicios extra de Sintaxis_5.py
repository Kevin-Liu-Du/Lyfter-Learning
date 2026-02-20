#Temperature Unit Converter
#Ask the user to enter a temperature in Celsius
#Convert it to Fahrenheit and Kelvin
#Display the three values

user = int(input("Enter a temperature in Celsius: "))
Fahrenheit = (user * 9/5) + 32
Kelvin = user + 273.15



print(f"The temperature is {user} °C.")
print(f"The temperature is {Fahrenheit} °F.")
print(f"The temperature is {Kelvin} °K.")