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
sql='SELECT * FROM personas'
#Uso del metodo execute
cursor.execute(sql)

#mostrar resultados
registro= cursor.fetchall()
#mostrar lista por consola
for fila in registro:
    print(fila)
#cerramos la conexion.
cursor.close()
conexion.close()