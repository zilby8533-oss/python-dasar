# List: berurutan dan bisa diubah
buah = ["apel", "jeruk", "mangga"]
buah.append("pisang")
buah.remove("jeruk")
print("List:", buah, "| jumlah:", len(buah))
print("Item pertama:", buah[0], "| terakhir:", buah[-1])

# Tuple: berurutan tapi tidak bisa diubah
koordinat = (10, 20)
x, y = koordinat
print("Tuple:", koordinat, "| x =", x, "y =", y)

# Set: unik dan tanpa urutan
angka = {1, 2, 3, 3, 2, 1}
angka.add(4)
print("Set:", angka)
a = {1, 2, 3}
b = {3, 4, 5}
print("Gabungan:", a | b)
print("Irisan:", a & b)
print("Selisih:", a - b)
