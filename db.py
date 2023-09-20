import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Doforit16'

)

curserObject = database.cursor()

curserObject.execute("CREATE DATABASE Notes")

print("all done")