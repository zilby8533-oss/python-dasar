# Tipe data dasar Python
umur = 17            # int
tinggi = 170.5       # float
nama = "Farhan"      # str
pelajar = True       # bool
kosong = None        # NoneType

for nilai in (umur, tinggi, nama, pelajar, kosong):
    print(nilai, "->", type(nilai).__name__)

# Konversi tipe data
print(int("25") + 5)
print(str(10) + " apel")
print(float(3))
print(bool(0), bool("ada"))
