from exercici32 import *

print("-----------Exercici 32-----------")
llista = []

for i in range(1, 11):
    llista.append(int(input(f"Número {i}: ")))

print(quadratLlista(llista))