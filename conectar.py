#conectar a una base de datos con el nombre del usuario SA y la clave 123456 y la base de datos es inventario y el servidor es localhost y el puerto es 1433

import pyodbc

conexion = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=TestDB;UID=SA;PWD=<YourStrong@Passw0rd>')

cursor = conexion.cursor()

cursor.execute("SELECT * FROM Inventory")

for fila in cursor:

    print(fila)

conexion.close()
