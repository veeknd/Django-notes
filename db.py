import mysql.connector
from decouple import config

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = config('passwd')

)

curserObject = database.cursor()

curserObject.execute("CREATE DATABASE IF NOT EXISTS Notes")

print("all done")