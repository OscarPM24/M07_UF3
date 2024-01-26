# Demanar a l’usuari que introdueixi 10 números separats per un espai. 
# Al acabar, el programa els introduirà en una tupla i els ordenarà (major o menor, com volgueu),
# mostrant per pantalla el contingut de la tupla.

values = input("Introdueix 10 numeros separats per un espai: ")
tupla = (values.split(' '))
print(sorted(tupla))