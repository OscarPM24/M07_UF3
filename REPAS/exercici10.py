# Crear un arxiu on caldrà endevinar el número escollit pel programa entre 1 i 100. 
# Cada vegada que l’usuari hi posi un número, caldrà indicar si és més petit o més gran 
# fins que encerti i el missatge haurà d’indicar que ha encertat. Indicar també el número d’intents.

import random

num = random.randint(1, 100)

numInput = 0
intents = 0

while numInput != num:
    numInput = int(input("Numero: "))
    
    if numInput < num:
        print("Més gran que", numInput)
    elif numInput > num:
        print("Més petit que", numInput)
    else:
        print("Encertat")
       
    intents+=1
    print("Intents:", intents)