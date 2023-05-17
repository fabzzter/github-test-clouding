#! /usr/bin/python3 

import sys
#Esta función dice Hola
def Saludo(n, s):
    print(n, s)


Saludo("hola", "chao")

print("Hola a todos")
print("Como estan?")
print("Chao!!!")

#Se imprime como una tupla
print("Hola a todos", "Como estan?", "Chao!!") 

#MEjor forma de imprimir varias lineas
print(
    """
    Hola a todos
    Como estan?
    Chao!!
    """)