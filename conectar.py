

import pyodbc

conexion = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=TestDB;UID=SA;PWD=<YourStrong@Passw0rd>')

cursor = conexion.cursor()

cursor.execute("SELECT * FROM Inventory")

for fila in cursor:

    print(fila)

conexion.close()
