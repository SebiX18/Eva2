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
        empleado_t = "INSERT INTO empleado(id, nombre, direccion, telefono, correo, fecha_inicio, salario, departamento_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        dato1 = (1, "Sebastian", "Av.Siempre viva", 940863864, "sebastian@gmail.com", "2020-05-12", 900000, 202)
        dato2 = (2, "Raul", "Mont", 973596244, "raulmatus22@gmail.com", "2021-01-15", 10000000, 69)
        departamento_t = "INSERT INTO departamento(id, nombre, descripcion, gerente_id) VALUES (%s, %s, %s, %s)"
        dato3 = (1, "Fufu", "Hardware", 1)
        dato4 = (2, "Rufu", "Software", 2)
        rol_t = "INSERT INTO rol (id, nombre, descripcion) VALUES (%s, %s, %s)"
        dato5 = (1, "Ejecutivo", "Manejar el personal dentro de cada departamento empresarial")
        dato6 = (2, "Empleado", "Recibe una contraprestación económica por sus servicios")
        permiso_t = "INSERT INTO permiso (id, nombre, descripcion) VALUES (%s, %s, %s)"
        dato7 = (1, "Ejecutivo", "Es admin")
        dato8 = (2, "Empleado", "Recibe ordenes del admin")
        rol_permiso = "INSERT INTO rol_permiso (rol_id, permiso_id) VALUES (%s, %s)"
        dato9 = (1,1)
        dato10 = (2,2)
        usuarioT = "INSERT INTO usuario (id, nombre_usuario, contraseña, rol_id) VALUES (%s, %s, %s, %s)"
        dato11 = (1, "Raul", 123, 1)
        dato12 = (2, "Sebastian", 123, 2)
        proyecto = "INSERT INTO proyecto (id, nombre, descripcion, fecha_inicio, fecha_fin) VALUES (%s, %s, %s, %s, %s)"
        dato13 = (1, "Steam", "Aplicacion para descargar juegos", "2008-02-28", "2050-12-12")
        dato14 = (2, "Twitch", "Apliacion para ver stream", "2014-01-22", "2028-09-01")
        empleado_proyecto = "INSERT INTO empleado_proyecto (empleado_id, proyecto_id) VALUES (%s, %s)"
        dato15 = (1,1)
        dato16 = (2,2)
        informe = "INSERT INTO informe (id, tipo_informe, fecha_creacion, empleado_id, departamento_id, proyecto_id) VALUES (%s, %s, %s, %s, %s, %s)"
        dato17 = (2, "Presencial", "2024-06-15", 2, 2, 1)
        dato18 = (1, "Presencial", "2024-10-18", 2, 2, 1)
        registrodetiempo = "INSERT INTO registrodetiempo (id, fecha, horas_trabajadas, descripcion, empleado_id, proyecto_id) VALUES (%s, %s, %s, %s, %s, %s)"
        dato19 = (1, "2024-11-29", 8, "Proceso de limpieza", 1, 1)
        dato20 = (2, "2024-04-25", 8, "Ayudante de la tienda", 2, 2)
        cursor.execute(registrodetiempo, dato20)
        conexion.commit()     

except Error as e:
    print(f"Error al conectar a MySQL: {e}")


finally:
    if conexion.is_connected():
        cursor.close()
        conexion.close()
        print("Conexión cerrada")        