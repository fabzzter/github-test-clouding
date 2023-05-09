numeros=[59,37,16,94,50,23,81,6,20]

# Forma de recorrer una lista con su indice
for num in enumerate(numeros):
    print(num)
for num in enumerate(numeros):
    indice=num[0]
    valor=num[1]
    print(f'El indice es: {indice} y el valor es: {valor}')
else:
    print('Bucle terminado!')