import math
import matematika
from matematika import tambah, kali
import matematika as mtk

print("import module:", matematika.tambah(2, 3))
print("from import:", tambah(10, 5), kali(4, 6))
print("alias:", mtk.luas_lingkaran(7))
print("module bawaan math:", math.sqrt(144), math.pi)
