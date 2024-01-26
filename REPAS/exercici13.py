# Demanar a l’usuari un número de l’1 al 10 i mostrar per pantalla la seva taula de multiplicar fins el 10. 
# Exemple: l’usuari marca 3, es mostra per pantalla: 3,6,9,12,15,18,21,24,27 i 30

num = int(input("Numero del 1 al 10: "))

for mult in range(1,11):
    print(num*mult)