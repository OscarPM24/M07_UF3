# Crear una funció que rebi un diccionari amb una llista de la compra (amb preus i descomptes).
# Exemple llista compra: {100:10, 250:5, 1500:30, …}
# on 100 és el preu i 20 el descompte a aplicar a aquests 100.
# Demanar a l’usuari l’IVA a aplicar al total de la llista de la compra.
# Mostrar per pantalla els valors amb el descompte aplicat més l’IVA.

def calculaTotalCompra(llista):
    iva = int(input("IVA? (4, 10 o 21): "))

    for preu, descompte in llista.items():
        preuFinal = (preu - (preu*(descompte/100))) 
        preuFinal += (preuFinal*(iva/100))
        print(f"Preu original: {preu}, Descompte: {descompte}%, IVA: {iva}%")
        print(f"Preu final: {preuFinal}")
        print("----------------------") 



