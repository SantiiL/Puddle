import mysql.connector
from mysql.connector import pooling
from settings import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT

# Establecemos la configuración de la conexión
config = {
  "user": DB_USER,
  "password": DB_PASSWORD,
  "host": DB_HOST,
  "port": DB_PORT,
  "database": DB_NAME
}

# Creamos una instancia de pool de conexiones
connection_pool = mysql.connector.pooling.MySQLConnectionPool(
    pool_name="puddle_pool",
    pool_size=5,
    **config
)

# Obtenemos una conexión del pool
connection = connection_pool.get_connection()

# Realizamos una consulta a la base de datos
cursor = connection.cursor()
cursor.execute("SELECT * FROM users")
results = cursor.fetchall()

# Cerramos la conexión y el cursor
cursor.close()
connection.close()