import connection

def readPortatiles():
    # Creamos un portatil
    sql = '''SELECT * FROM PORTATILES'''

    # Enviamos la query con el método execute()
    connection.connection.execute(sql)

    # Usamos el método fetchall() para obtener todos los datos de la query
    lista_portatiles = connection.connection.fetchall()
    print("Mostrando los portatiles de la Base de Datos...")
    
    # Print de creación de tabla exitosa
    for portatil in lista_portatiles:
        print('\n',portatil)        

