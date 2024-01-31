# Igual que l’anterior però a la tupla afegir la frase sense 
# els caràcters repetits i mostrar el contingut de la tupla. 
# Exemple: Usuari indica la paula caracteristica. Es mostra per pantalla carteis.
frase = input("Introdueix una frase: ")
tupla = tuple(set(frase))
print(tupla)
