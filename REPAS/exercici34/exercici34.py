# Crear una funció que rebi, per paràmetres, una funció i una llista. 
# Ha de crear una llista nova amb el nou contingut i mostrar-la per pantalla.
# Passes:
# Crear una funció que calculi el quadrat d’un número passat per paràmetre.
# Crear una segona funció que agafi cada número de la llista (passat per paràmetre) 
# i truqui a la funció anterior i guardar el resultat a una llista.


def calculaQuadrat(num):
    return num**2

def convertirLlista(calculaQuadrat, llista):
    llistaQuadrat = []
    
    for num in llista:
        llistaQuadrat.append(calculaQuadrat(num))
        
    print(llistaQuadrat)






