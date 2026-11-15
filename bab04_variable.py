# Variable di Python
nama = "Farhan"
kelas = "XI"
print(nama, kelas)

# Mengisi banyak variable sekaligus
x, y, z = 1, 2, 3
print(x, y, z)

# Satu nilai untuk beberapa variable
a = b = c = 0
print(a, b, c)

# Menukar nilai tanpa variable bantu
x, y = y, x
print("Setelah ditukar:", x, y)

# Variable bisa diubah nilai dan tipenya
data = 10
print(data, type(data).__name__)
data = "sepuluh"
print(data, type(data).__name__)

# Penamaan: huruf kecil dipisah garis bawah
nama_lengkap = "Farhan Arya Zaelani"
print(nama_lengkap)
