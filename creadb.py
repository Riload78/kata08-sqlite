import sqlite3

# establecer la conexion
connection = sqlite3.connect("data/movements.db")

# Creamos el cursor (es un objeto que nos permite las funcionalidades para operar con la BBDD)
cur = connection.cursor()

f = open("data/create.sql", 'r')
query = f.read()


print(query)

try:
    cur.execute(query)
except sqlite3.Error as e:
    print('Error de SQL:',e.args[0])