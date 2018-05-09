import pymysql

connection = pymysql.connect(user='root', password = 'password', host = 'localhost')
c = connection.cursor

c.execute("CREATE SCHEMA pythontut")

c.close()

connection.close()
