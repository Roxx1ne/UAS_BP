import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = "",
    database = "databasenomorlima",
)

if database.is_connected():
    print("Sudah Terkoneksi")
