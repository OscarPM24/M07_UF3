# Demanar a l’usuari que posi dues paraules. Al executar el programa, 
# mostrarà per pantalla les dues paraules amb els dos primers caràcters
# de cada paraula intercanviats. Exemple: Quatre Camins passaria a Caatre Qumins.

paraula1 = input("Paraula 1: ")
paraula2 = input("Paraula 2: ")

inicial1 = paraula1[:2]
inicial2 = paraula2[:2]

paraula1 = inicial2 + paraula1[2:]
paraula2 = inicial1 + paraula2[2:]
print(paraula1, paraula2)