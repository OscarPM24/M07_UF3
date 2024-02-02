# Crear una funció que rebi una frase per paràmetre. Aquesta frase es demana a l’usuari. 
# Ha de retornar un diccionari amb les paraules que conte i la longitud de cada paraula.

def fraseDiccionari(frase):
    diccionari = {}
    paraules = frase.split(" ")
    
    for paraula in paraules:
        diccionari[paraula] = len(paraula)
    
    return diccionari