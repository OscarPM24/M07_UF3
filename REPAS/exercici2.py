# Demanar a l’usuari que introdueixi un valor en €, 
# seguidament demanar que introdueixi el IVA a aplicar-hi (4%, 10% o 21%) 
# i finalment mostrar, per pantalla, el resultat del valor indicat per l’usuari, 
# el % d’IVA demanat per l’usuari i el valor final amb l’IVA afegit.
valor = int(input("Valor en €:"))
iva = int(input("IVA (4, 10 o 21):"))
valorIVA = valor + valor * iva / 100
print(f"Valor: {valor}, IVA: {iva}, valor amb IVA: {valorIVA}")