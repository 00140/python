from flask import Flask, jsonify
import psycopg2
from psycopg2 import sql

app = Flask(__name__)

# Configura los parámetros de la conexión a la base de datos
DB_HOST = 'localhost'
DB_NAME = 'tu_base_de_datos'
DB_USER = 'tu_usuario'
DB_PASSWORD = 'tu_contraseña'

def get_db_connection():
    conn = psycopg2.connect(
        host='192.168.1.30',
        dbname='postgres',
        user='postgres',
        password='123'
    )
    return conn

@app.route('/data', methods=['GET'])
def get_data():
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Realiza una consulta en la base de datos
    cur.execute('SELECT * FROM cotizacion.serigrafia_precio_material;')  # Sustituye 'tu_tabla' con el nombre de tu tabla
    rows = cur.fetchall()
    
    # Crea un diccionario con los resultados
    columns = [desc[0] for desc in cur.description]
    result = []
    for row in rows:
        result.append(dict(zip(columns, row)))
    
    cur.close()
    conn.close()
    
    # Devuelve los resultados en formato JSON
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
