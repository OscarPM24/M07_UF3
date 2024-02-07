import psycopg2

# Credenciales del docker-compose.yml
conn = psycopg2.connect(
    database='practica2_bd',
    user='oscar',
    password='system',
    host='localhost',
    port='5432'
)

# Cursor para hacer la conexión a la bd
connection = conn.cursor()

# Print del cursor para ver si funciona bien
print(connection)