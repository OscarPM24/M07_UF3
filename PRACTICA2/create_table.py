import connection

def creaTabla():
    # Borramos la tabla portatiles
    sql_drop = '''DROP TABLE IF EXISTS PORTATILES'''
    
    # Creamos la tabla portatiles
    sql_create = '''CREATE TABLE IF NOT EXISTS PORTATILES(
                id SERIAL PRIMARY KEY,
                marca VARCHAR(255) NOT NULL,
                modelo VARCHAR(255) NOT NULL,
                procesador VARCHAR(255) NOT NULL,
                memoria_ram BIGINT NOT NULL,
                pulgadas FLOAT NOT NULL,
                sistema VARCHAR(255) NOT NULL
    )'''

    # Enviamos las querys con el método execute()
    connection.connection.execute(sql_drop)
    connection.connection.execute(sql_create)

    # Usamos el método commit() para ejecutar los cambios a la BD
    connection.conn.commit()
    
    # Print de creación de tabla exitosa
    print("Tabla portatiles creada exitosamente!")

