#importacion de modulo
import psycopg2
#conexion a la base de datos.
conexion = psycopg2.connect(user='postgres',
                    password='1941',
                    host='127.0.0.1',
                    port='5432',
                    database='test_db')
#Objetos que nos permite realizar consulta.
cursor = conexion.cursor()
#sentencia sql
sql=' UPDATE personas SET nombre=%s,apellido=%s,dni=%s WHERE idpersona=%s'

#Consulta datos usuario.
idpersona=input('ingrese id de la persona a editar: ')
nombre = input('ingrese nombre: ')
apellido= input('ingrese apellido: ')
dni= input('ingrese dni: ')
#recoleccion de datos.
datos= (nombre,apellido,dni,idpersona)
#hacemos uso del metodo execute
cursor.execute(sql,datos)
#guardamos los datos del registro.
conexion.commit()
#contar el numero de cambios
actualizacion =cursor.rowcount
#mostrar por consola
print(f'registro actualizado: {actualizacion}')
#cerramos la conexion.
cursor.close()
conexion.close()
