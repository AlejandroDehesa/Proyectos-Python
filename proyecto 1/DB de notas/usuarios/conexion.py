# Importar el conector de MySQL
import mysql.connector

def conectar():
    # Conectar a la base de datos
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="master_python",
        port=3306
    )

    # Crear un cursor para ejecutar consultas
    cursor = database.cursor(buffered=True)
    
    # Devolver la conexión y el cursor
    return [database, cursor]
