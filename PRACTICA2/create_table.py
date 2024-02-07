import connection

# Creamos la tabla portatiles
sql = '''CREATE TABLE PORTATILES(
            id SERIAL PRIMARY KEY,
            marca VARCHAR(255) NOT NULL
            modelo VARCHAR(255) NOT NULL
            procesador VARCHAR(255) NOT NULL
            memoria_ram BIGINT NOT NULL
            pulgadas FLOAT NOT NULL
            sistema VARCHAR(255) NOT NULL
)'''

# Enviamos la query con el método execute()
connection.execute(sql)
print(connection)
# Usamos el método commit() para ejecutar los cambios a la BD

