# Crear una tupla amb els mesos de l’any. Demanar a l’usuari que posi un número entre 0 i 12 
# i mostrar per pantalla el mes corresponent al número indicat per l’usuari. 
# El programa finalitza només quan l’usuari posa 0.

mesos = ('Gener', 'Febrer', 'Març', 'Abril', 'Maig', 'Juny', 'Juliol', 'Agost', 'Setembre', 'Octubre', 'Novembre', 'Desembre')
num = int(input("Numero entre 0 i 12: "))

while num != 0:
    print(mesos[num-1])
    num = int(input("Numero entre 0 i 12: "))