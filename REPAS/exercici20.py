# Crear un diccionari on la clau (key) sigui un nom i el valor (value) l’edat. 
# S’haura de demanar a l’usuari que posi contactes (noms i edats). 
# Si algun nom es repeteix no s’fageirà al diccionari (indicant-ho a l’usuari). 
# Es deixarà d’inserir contactes quan l’usuari indiqui que no vol afegir-ne més.

contactes = {}
nom = input("Insereix nom: ")
edat = input("Insereix edat: ")

while (len(nom) != 0):
    if nom in contactes:
        print("Aquest nom ja existeix")
    else:
        contactes[nom] = edat
        print(contactes)
    nom = input("Insereix nom: ")
    edat = input("Insereix edat: ")
    