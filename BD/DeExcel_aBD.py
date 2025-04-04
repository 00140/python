import psycopg2
from psycopg2.extras import execute_values
import pandas as pd

# Leer el archivo CSV
df = pd.read_csv('/home/erick/Documentos/BDLIBROSSQL.csv')

# Verifica las columnas y la forma del DataFrame
print(df.columns)
print(df.shape)  # Te dirá cuántas filas y columnas tiene el DataFrame

# Convertir los datos a numéricos (si no pueden ser convertidos, los pone como NaN)
#df = df.apply(pd.to_numeric, errors='coerce')

# Manejar valores NaN si es necesario, por ejemplo, reemplazándolos por None
#df = df.where(pd.notnull(df), None)

# Ver los primeros registros
print(df)

# Configurar la conexión
try:
    conn = psycopg2.connect(
        dbname="biblioteca",
        user="bibliotecario",
        password="aa",
        host="192.168.1.30",
        port="5432"
    )
    cursor = conn.cursor()

    # Definir la consulta para insertar los registros, omitiendo el campo id
    insert_query = """
        INSERT INTO blt.libros(titulo, autor, genero, estatus)
        VALUES %s
    """

    # Convertir el DataFrame a una lista de tuplas con enteros
    #data = [tuple(map(lambda x: None if pd.isnull(x) else int(x), row)) for row in df.values]
    data = [tuple(map(lambda x: None if pd.isnull(x) else (x), row)) for row in df.values]
    #data = [tuple(row) for row in df.values]

    # Verificar los primeros datos a insertar
    print(data[:5])

    # Ejecutar la inserción de datos
    execute_values(cursor, insert_query, data)

    # Confirmar la transacción
    conn.commit()

except Exception as e:
    print(f"Error: {e}")

finally:
    cursor.close()
    conn.close()
