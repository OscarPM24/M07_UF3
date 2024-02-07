import connection

def creaPortatil():
    # Creamos un portatil
    sql = '''INSERT INTO PORTATILES(marca, modelo, procesador, memoria_ram, pulgadas, sistema) VALUES (
        'Asus', 'VivoBook', 'i7-1065G7', 8, 14.5, 'Windows'
        )'''

    # Enviamos la query con el método execute()
    connection.connection.execute(sql)

    # Usamos el método commit() para ejecutar los cambios a la BD
    connection.conn.commit()
    
    # Print de creación de tabla exitosa
    print('Portatil creado exitosamente!')

