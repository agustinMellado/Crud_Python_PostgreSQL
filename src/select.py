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
sql='SELECT * FROM personas WHERE idpersona=%s'
#solicitar datos al usuario
idpersona= input('ingrese el id del registro persona que quiere mostrar: ')
#Uso del metodo execute
cursor.execute(sql,idpersona)

#muestro un solo resultado
registro= cursor.fetchone()
#mostrar lista por consola
print(registro)
#cerramos la conexion.
cursor.close()
conexion.close()