import psycopg2
#conexion a la base de datos.
conexion = psycopg2.connect(user='postgres',
                    password='1941',
                    host='127.0.0.1',
                    port='5432',
                    database='test_db')
#Objetos que nos permite realizar consulta
cursor = conexion.cursor()
#Creacion de consulta
consulta = 'SELECT * FROM personas'
cursor.execute(consulta) #ejecucion de consulta.  
registros = cursor.fetchall()  #obtenemos el registro, tomado de la consulta
print(registros) #imprimimos el registro

#cerramos la conexion.
cursor.close()
conexion.close()


