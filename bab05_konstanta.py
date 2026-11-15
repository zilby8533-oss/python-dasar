# Konstanta di Python
# Python tidak punya konstanta sungguhan, jadi dipakai konvensi huruf kapital
from typing import Final

PI = 3.14159
GRAVITASI = 9.8
NAMA_SEKOLAH: Final = "SMK Contoh"

jari_jari = 7
luas = PI * jari_jari ** 2
print("Luas lingkaran:", luas)
print("Gravitasi:", GRAVITASI, "m/s^2")
print("Sekolah:", NAMA_SEKOLAH)

# Final hanya petunjuk untuk alat bantu seperti mypy, bukan penghalang saat dijalankan
