# Demanar a l’usuari que posi 10 números separats per espais. 
# Afegir aquests números a una llista. Calcular la suma de tots els números 
# i la seva mitjana i afegir aquests 2 números a la llista. Mostrar per pantalla la llista.

# Exemple mostra per pantalla.
# Números de l’usuari:
# suma total:
# mitjana:

numeros = input("Introdueix 10 numeros separats per espais: ")
llista = list(numeros.split(" "))

print("Números de l'usuari:", llista)

suma = 0
for num in llista:
    suma += int(num)

print("Suma total:", suma)
print("Mitjana:", suma/len(llista))