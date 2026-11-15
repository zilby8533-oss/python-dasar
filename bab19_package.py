from alat import hitung, teks
from alat.teks import balik
import random
import datetime

nilai = [80, 90, 75, 85]
print("Rata-rata:", hitung.rata_rata(nilai))
print("Maksimum:", hitung.maksimum(nilai))
print(teks.kapital("belajar python itu menyenangkan"))
print(balik("python"))
print("Standard library -> angka acak:", random.randint(1, 10))
print("Standard library -> tanggal:", datetime.date.today())
