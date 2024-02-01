# Crear una funció que retorni un XML (crear arxiu .xml i mostrar per consola l’XML). 
# La funció ha de crear l’XML, crear les etiquetes i inserir text segons les següents especificacions:

# Un root de nom students.
# Cinc childs (del root) amb nom student.
# Cada child student ha de tindre 4 subchilds:
#  name
#  surname
#  email
#  dni
# Ha d’haver-hi un atribut (amb nom i valor) a dintre de cada element child “student”.
# El text de cada etiqueta serà de la vostra elecció.

import xml.etree.ElementTree as ET

def crearXML():
    students = ET.Element('students')

    for i in range(1,6):
        
        student = ET.SubElement(students, 'student')
        
        name = ET.SubElement(student, 'name')
        surname = ET.SubElement(student, 'surname')
        email = ET.SubElement(student, 'email')
        dni = ET.SubElement(student, 'dni')
        
        name.text = f"nom {i}"
        surname.text = f"cognom {i}"
        email.text = f"correu {i}"
        dni.text = f"dni {i}"

    ET.indent(students)

    tree = ET.ElementTree(students)
    tree.write('students.xml')

    ET.dump(students)

crearXML()