import mysql.connector
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="root",
database="mysql",
port='3307'
)
cursor = mydb.cursor()
cursor.execute("Show Databases;")
res = cursor.fetchall()
print(res)