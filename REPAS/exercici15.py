# El mateix que l’anterior exercici, però sense demanar un màxim de números. 
# L’usuari indicarà quan ha acabat posant un 0.

values = ""
num = input("Introdueix numero: ")

while num != "0":
    values = values + num
    num = input("Introdueix numero: ")
    
print(sorted(tupla))