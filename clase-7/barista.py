# robot barista

menu = "Café, té o agua"
price = 4
stock = 50

print("Hola, bienvenido a la cafeteria de Fabrizzio")
name = input("Cual es tu nombre? \n")
order = input("Hola " + name + ", que desea ordenarde nuestro menú \n" + menu + "\n")
quantity = input("Cuantas unidades deseas? \n")
if (int(quantity) > stock):
    print(f"Lo lamentamos, pero solo tenemos {quantity} unidades de {order}")
else:
    bill = int(quantity) * int(price)
    print(f"El valor total de tu orden es: ${bill}")