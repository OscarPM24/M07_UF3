import connection

def creaTabla():
    # Creamos la tabla portatiles
    sql = '''CREATE TABLE IF NOT EXISTS PORTATILES(
                id SERIAL PRIMARY KEY,
                marca VARCHAR(255) NOT NULL,
                modelo VARCHAR(255) NOT NULL,
                procesador VARCHAR(255) NOT NULL,
                memoria_ram BIGINT NOT NULL,
                pulgadas FLOAT NOT NULL,
                sistema VARCHAR(255) NOT NULL
    )'''

    # Enviamos la query con el método execute()
    connection.connection.execute(sql)

    # Usamos el método commit() para ejecutar los cambios a la BD
    connection.conn.commit()
    
    # Print de creación de tabla exitosa
    print("Tabla portatiles creada exitosamente!")

