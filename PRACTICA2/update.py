import connection

def updatePortatil(index, columna, valor):
    # Editamos un portatil, el índice, columna y valor se pasan por parámetros
    sql = f'''UPDATE PORTATILES SET {columna} = '{valor}' WHERE id = {index}'''

    # Enviamos la query con el método execute()
    connection.connection.execute(sql)

    # Usamos el método commit() para ejecutar los cambios a la BD
    connection.conn.commit()
    
    # Print de actualización de portatil exitoso
    print(f'Portatil actualizado exitosamente! ({columna} -> {valor})')

