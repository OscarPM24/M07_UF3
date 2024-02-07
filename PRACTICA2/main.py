# Imports
import psycopg2
from connection import *
from create_table import *

try:
    # Conexión a la BD
    connection
    print()
    
    # Creación de la tabla portatiles
    response = input("Quieres crear la tabla de portatiles? (y/n) ")
    if response == 'y':
        creaTabla()


except (Exception, psycopg2.Error) as error:
    # Print del error
    print("Error:", error)

finally:
    # Cerramos la conexión a la BD
    conn.close()
