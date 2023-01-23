import mysql.connector

# ngekoneksi ke databasenya
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="databasenomorlima"
)

cursor = cnx.cursor()
# Membuat tabelnya
create_table = """
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    pendidikan_terakhir varchar(255),
    profesi varchar(255),
    kelamin varchar(255),
    jabatan varchar(255)
)
"""
cursor.execute(create_table)

# Menambahkan data
add_user = "INSERT INTO users (nama, email, pendidikan_terakhir, profesi, kelamin, jabatan) VALUES (%s, %s, %s, %s, %s, %s, %s)"
cursor.execute(add_user)
cnx.commit()

# Mengambil data
query = "SELECT * FROM users"
cursor.execute(query)

for (id, name, email, pendidikan_terakhir, profesi, kelamin, jabatan) in cursor:
    print("ID: {}, Name: {}, Email: {}, Pendidikan_terakhir: {}, Profesi: {}, Kelamin: {}, Jabatan: {} ".format(id, name, email, pendidikan_terakhir, profesi, kelamin, jabatan))

# Menutup koneksi
cursor.close()
cnx.close()
