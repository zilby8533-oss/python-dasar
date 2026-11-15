# try - except
try:
    hasil = 10 / 0
except ZeroDivisionError:
    print("Error: tidak bisa dibagi nol")

# Beberapa jenis error
for data in ["25", "abc", 0]:
    try:
        print("Hasil:", 100 / int(data))
    except ValueError:
        print("Error: bukan angka ->", data)
    except ZeroDivisionError:
        print("Error: pembagi nol")
    else:
        print("Tidak ada error untuk", data)
    finally:
        print("Selesai memproses", data)

# raise: membuat error sendiri
def cek_umur(umur):
    if umur < 0:
        raise ValueError("Umur tidak boleh negatif")
    return umur

try:
    cek_umur(-5)
except ValueError as e:
    print("Error ditangkap:", e)
