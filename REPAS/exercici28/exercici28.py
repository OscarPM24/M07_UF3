# Crear una funció que passats dos números per paràmetre (demanats a l’usuari) 
# ens mostri per pantalla un número aleatori entre aquests dos números.
import random

def numerosAleatoris(num1, num2):
    print(random.randint(num1, num2))