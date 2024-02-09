try:
    # Imports
    import psycopg2
    from connection import *
    from create_table import *
    from create import *
    from read import *
    from update import *

    # Conexión a la BD
    connection
    
    # Creación de la tabla portatiles
    response = input("\nQuieres crear la tabla de portatiles? (y/n) ")
    if response == 'y':
        creaTabla()

    select = 1
    while select != 0:
        select = int(input('\nMenú de selección (1 Create, 2 Read, 3 Update, 4 Delete, 0 Salir) '))
        if select == 1:
            createPortatil()
        elif select == 2:
            readPortatiles()
        elif select == 3:
            updatePortatil(1, "sistema", "Linux")
        # elif select == 4:
        #     # delete
            

except (Exception, psycopg2.Error) as error:
    # Print del error
    print("Error:", error)

finally:
    # Cerramos la conexión a la BD
    conn.close()
