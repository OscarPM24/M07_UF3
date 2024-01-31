# Demanar a l’usuari posar 2 paraules. Afegir aquestes a una tupla 
# i mostrar per pantalla quantes vegades apareix cada lletra.

frase = input("Introdueix 2 paraules: ")
tupla = tuple(frase.replace(" ", ""))
lletres = set(tupla)

for letra in lletres:
    print(letra, ":", tupla.count(letra))