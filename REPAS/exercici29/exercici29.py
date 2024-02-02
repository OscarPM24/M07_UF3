# Crear una funció que passats dos números per paràmetre (demanats a l’usuari) 
# ens mostra per pantalla tots els números (enters) que hi ha entre ells. 
# També mostrarà per pantalla la suma d’aquests números enters.

def numerosEnters(num1, num2):
    suma = 0
    
    for i in range(num1, num2+1):
        print(i)
        suma += i
        
    print("Suma:",suma)
        