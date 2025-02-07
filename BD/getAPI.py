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
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return conn

@app.route('/data', methods=['GET'])
def get_data():
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Realiza una consulta en la base de datos
    cur.execute('SELECT * FROM cotizacion.serigrafia_precio_millar;')  
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
