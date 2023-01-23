print("CONTOH EROR ZERODIVISION ")
a = 2
b = 0
hasil = a/b

print("/n")

print("CONTOH EROR NAMEEROR")

def nameeror():
    try:
        kalimat = "Halooo dunia"
        return IniContohReturnEror
    except nameeror:
        return "fungsi nameeror terjadi eror, karena variabel kalimat tidak di definisikan"
 
print(nameeror())

print("/n")

print("CONTOH TYPEROR ")
TipeDataInt = 100
TipeDataStr = "haloo"
hasil = TipeDataInt/TipeDataStr
print(hasil)
