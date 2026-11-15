class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi ** 2

class Lingkaran:
    def __init__(self, jari):
        self.jari = jari

    def luas(self):
        return 3.14 * self.jari ** 2

class Segitiga:
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def luas(self):
        return 0.5 * self.alas * self.tinggi

# Satu pemanggilan yang sama, hasil sesuai jenis object
for bentuk in [Persegi(4), Lingkaran(7), Segitiga(6, 5)]:
    print(type(bentuk).__name__, "luas =", bentuk.luas())

# Fungsi len bekerja pada banyak tipe data
print(len("Python"), len([1, 2, 3]), len({"a": 1}))
