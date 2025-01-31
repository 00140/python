import psycopg2

# Parámetros de conexión
host = "jdbc:postgresql://localhost:5432"  # Dirección del servidor de la base de datos
database = "biblioteca"  # Nombre de la base de datos
user = "bibliotecario"  # Tu usuario de PostgreSQL
password = "aa"  # Tu contraseña

# Establecer la conexión
try:
    conn = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )

    # Crear un cursor para ejecutar consultas
    cur = conn.cursor()

    # Realizar una consulta de prueba
    cur.execute("SELECT version();")
    db_version = cur.fetchone()
    print("Conectado a la base de datos:", db_version)

    # Cerrar el cursor y la conexión
    cur.close()
    conn.close()

except Exception as e:
    print("Error al conectar a la base de datos:", e)