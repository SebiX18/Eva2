import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="prueba",
        port=3306
    )

    if conexion.is_connected():
        print("Conexión exitosa a la base de datos")
        cursor = conexion.cursor()
        

except Error as e:
    print(f"Error al conectar a MySQL: {e}")


finally:
    if conexion.is_connected():
        cursor.close()
        conexion.close()
        print("Conexión cerrada")        