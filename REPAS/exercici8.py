# Demanar a l’usuari que posi entre 1 i 3 paraules. Al executar el programa, 
# mostrarà la/es paraula/es indicada/es per l’usuari, 
# indicar quants caràcters té i indicar el primer, i l’últim caràcter.

text = input("Escriu entre 1 i 3 paraules: ")
print("Paraules posades: " + text)
print("Caràcters:", len(text))
print("Primer caràcter:", text[0])
print("Últim caràcter:", text[-1])