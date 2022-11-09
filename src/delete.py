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
#Sentencia sql
sql= 'DELETE FROM personas WHERE idpersona = %s' #elimina segun el id que importemos

#solicitar dato al usuario
idpersona= input('ingrese el id del registro a eliminar: ')

#metodo execute
cursor.execute(sql, idpersona)

#guardar los cambios en la bd
conexion.commit()

#Conteo de registro eliminado
registro_eliminado = cursor.rowcount

#mensaje al usuario
print(f'registros eliminados: {registro_eliminado}')
#cerrar conexiones 
cursor.close()
conexion.close()