# Crear una funció per calcular el total d’una factura amb l’IVA. 
# La funció ha de rebre (per paràmetre) la quantitat sense IVA i l’IVA a aplicar (introduïts per l’usuari). 
# En cas de no passar-li cap valor o un valor erroni (4%, 10% o 21%) s’aplicarà directament el 21%. 
# Es mostra per pantalla el valor sense IVA, l’IVA i el total.

def calculaTotal(quantitat, iva):
    print(iva)
    if (iva==4 or iva==10 or iva==21):    
        iva = iva
    else:
        iva = 21
    
    quantitatIva = quantitat + (quantitat * (iva/100))
    
    print("Valor sense IVA:",quantitat)
    print("IVA:",iva)
    print("Total:",quantitatIva)
    