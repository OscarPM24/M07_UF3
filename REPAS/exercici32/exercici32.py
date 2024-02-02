# Crear una funció que agafi una llista amb 10 números, 
# i retorni una altra llista amb els seus quadrats.

def quadratLlista(llista):
    llistaQuadrats = []
    
    for i in range(0, len(llista)):
        llistaQuadrats.append(llista[i]**2)
    
    return llistaQuadrats