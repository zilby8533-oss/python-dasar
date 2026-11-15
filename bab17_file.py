# Menulis file
with open("catatan.txt", "w") as f:
    f.write("Baris pertama\n")
    f.write("Baris kedua\n")

# Menambah isi file
with open("catatan.txt", "a") as f:
    f.write("Baris ketiga\n")

# Membaca seluruh isi
with open("catatan.txt", "r") as f:
    print("Isi file:")
    print(f.read())

# Membaca per baris
with open("catatan.txt") as f:
    for nomor, baris in enumerate(f, start=1):
        print(nomor, baris.strip())
