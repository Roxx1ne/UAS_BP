import mysql.connector
import tkinter as tk

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="databasenomorlima"
)

# Create a cursor
cursor = conn.cursor()

# Function to insert data into the database
def insert_data():
    id = entry_id.get()
    name = entry_name.get()
    email = entry_email.get()
    pendidikan_terakhir = entry_pendidikan_terakhir.get()
    profesi = entry_profesi.get()
    kelamin = entry_kelamin.get()
    jabatan = entry_jabatan.get()
    cursor.execute("INSERT INTO users (id, name, email, pendidikan_terakhir, profesi, kelamin, jabatan) VALUES (%s, %s, %s, %s, %s, %s, %s)", (id, name, email, pendidikan_terakhir, profesi, kelamin, jabatan))
    conn.commit()
    label.config(text="Data inserted successfully!")

# Function to fetch data from the database
def fetch_data():
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    return results

# GUI
root = tk.Tk()
root.title("Database App")

label = tk.Label(root, text="Enter user information:")
label.grid(row=0, column=0, columnspan=2)

id_label = tk.Label(root, text="ID:")
id_label.grid(row=1, column=0)
entry_id = tk.Entry(root)
entry_id.grid(row=1, column=1)

name_label = tk.Label(root, text="Name:")
name_label.grid(row=2, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=2, column=1)

email_label = tk.Label(root, text="Email:")
email_label.grid(row=3, column=0)
entry_email = tk.Entry(root)
entry_email.grid(row=3, column=1)

pendidikan_terakhir_label = tk.Label(root, text="Pendidikan_terakhir:")
pendidikan_terakhir_label.grid(row=4, column=0)
entry_pendidikan_terakhir = tk.Entry(root)
entry_pendidikan_terakhir.grid(row=4, column=1)

profesi_label = tk.Label(root, text="Profesi:")
profesi_label.grid(row=5, column=0)
entry_profesi = tk.Entry(root)
entry_profesi.grid(row=5, column=1)

kelamin_label = tk.Label(root, text="Kelamin:")
kelamin_label.grid(row=6, column=0)
entry_kelamin = tk.Entry(root)
entry_kelamin.grid(row=6, column=1)

jabatan_label = tk.Label(root, text="Jabatan:")
jabatan_label.grid(row=7, column=0)
entry_jabatan = tk.Entry(root)
entry_jabatan.grid(row=7, column=1)

insert_button = tk.Button(root, text="Insert", command=insert_data)
insert_button.grid(row=8, column=0, columnspan=2)

root.mainloop()
