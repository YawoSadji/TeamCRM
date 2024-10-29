import mysql.connector

connection = mysql.connector.connect(
    user='root',
    password='password123',
    host='localhost'
)
cursor = connection.cursor()
cursor.execute("CREATE DATABASE crmdatabase")
print("Done")