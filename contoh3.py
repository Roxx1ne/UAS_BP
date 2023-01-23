import tkinter as tk 
def on_button_click():
    label.config(text = " Tombol di tekan ")

root = tk.Tk()
root.title("Contoh GUI dengan Tkinter ")

label = tk.Label(root, text = " Tekan tombol di bawah ini ")
label.pack()

button = tk.Button(root, text= " Tekan Tombol ini ", command=on_button_click)
button.pack()

root.mainloop()
