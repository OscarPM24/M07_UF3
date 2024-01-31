# El mateix que l’anterior exercici, però sense demanar un màxim de números. 
# L’usuari indicarà quan ha acabat posant un 0.

tupla = ()
num = input("Introdueix numero: ")

while num != "0":
    tupla += tuple(num)
    num = input("Introdueix numero: ")
    
print(tuple(sorted(tupla)))