# Buscar error/s en el següent programa:

def amb_iva(ftotal, iva = 21):
    ftotal += ftotal * (iva/100)    
    return ftotal 

ftotal = int(input('Introdueix el preu de tot el carrito: '))

print(amb_iva(ftotal, iva = 21))


