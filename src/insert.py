import psycopg2
#conexion a la base de datos.
conexion = psycopg2.connect(user='postgres',
                    password='1941',
                    host='127.0.0.1',
                    port='5432',
                    database='test_db')
#Objetos que nos permite realizar consulta.
cursor = conexion.cursor()
#Creacion de consulta.
sql= 'INSERT  INTO  personas (nombre, apellido, dni) VALUES  (%s,%s,%s)'
#solicitud de datos al usuario.
nombre = input('ingrese nombre: ')
apellido= input('ingrese apellido: ')
dni= input('ingrese dni: ')
#recoleccion de datos.
datos= (nombre,apellido,dni)
#hacemos uso del metodo execute
cursor.execute(sql,datos)
#guardamos los datos del registro.
conexion.commit()
#registro insertado
registros= cursor.rowcount
#mostrar por pantalla
print(f'registro insertado {registros}')

#cerramos la conexion.
cursor.close()
conexion.close()
