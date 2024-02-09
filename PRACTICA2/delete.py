import connection

def deletePortatil(index):
    # Eliminamos un portatil, el índice se pasa por parámetro
    sql = f'''DELETE FROM PORTATILES WHERE id = {index}'''

    # Enviamos la query con el método execute()
    connection.connection.execute(sql)

    # Usamos el método commit() para ejecutar los cambios a la BD
    connection.conn.commit()
    
    # Print de eliminación de portatil exitoso
    print('Portatil eliminado exitosamente!')

