import sqlite3
# creamos la conexio
connection = sqlite3.connect('data/movements.db')
#creamos el cursor
cur = connection.cursor()
# Creamos la quury
query = "INSERT INTO movements values(NULL,'2023-01-05','Sueldo',1000,'EUR')"

#ejecutamos la query
cur.execute(query)


# Query dinamica

query2 = '''
    INSERT INTO movements (date, abstract,amount,currency) values(?,?,?,?,)
'''

fecha = "1970-03-04"
concepto = "Sobresuledo"
cantidad = 2000
currency = 'EUR' 

cur.execute(query, (fecha,concepto,cantidad,currency))

cur.execute(query2)



# Confirmamos la consulta -> si no se hace el commit se pierde la consulta
connection.commit()