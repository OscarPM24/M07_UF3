# Cal buscar la informació que es demana de la següent list:
# areas_pis = [“Menjador”, 10.15, “Rebedor”, 9.56, “Habitació1”, 12.34, “Terrassa”, 15.55, “Lavabo”, 7.98, “Cuina”, 12, “Habitació2”, 12.23]
# (Cal utilitzar els “:” per a que siguin vàlids els prints següents)
# Imprimir el segon element
# Imprimir l’últim element
# Imprimir l’àrea de la terrassa
# Imprimir del primer element al tercer element
# Imprimir del tercer element a l’últim
# Imprimir el total de l'àrea de les dues habitacions
# Modificar l’àrea del lavabo i imprimir la nova list area
# Afegir l'àrea de “pati interior” i 2.78 a les últimes posicions. Imprimir la nova list area.
# Imprimir el total de l’àrea del pis.

areas_pis = ["Menjador", 10.15, "Rebedor", 9.56, "Habitació1", 12.34, "Terrassa", 15.55, "Lavabo", 7.98, "Cuina", 12, "Habitació2", 12.23]

print("Segon element:", areas_pis[1:2])
print("Ultim element:", areas_pis[-1:])
print("Area terrassa:", areas_pis[areas_pis.index("Terrassa")+1: areas_pis.index("Terrassa")+2])
print("1r a 3r element:", areas_pis[0:3])
print("3r a ultim element:", areas_pis[2:])
print("Total area habitacions:", areas_pis[areas_pis.index("Habitació1")+1] + areas_pis[areas_pis.index("Habitació2")+1])
areas_pis[areas_pis.index("Lavabo")+1] = 10
print(areas_pis)
areas_pis.extend(["Pati inferior", 2.78])
print(areas_pis)
print(areas_pis[1] + areas_pis[3] + areas_pis[5] + areas_pis[7] + areas_pis[9] + areas_pis[11] + areas_pis[13] + areas_pis[15])