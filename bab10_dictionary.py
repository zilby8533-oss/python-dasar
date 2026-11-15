siswa = {"nama": "Farhan", "kelas": "XI", "nilai": 85}
print(siswa)
print("Nama:", siswa["nama"])
print("Umur:", siswa.get("umur", "tidak ada"))

siswa["nilai"] = 90
siswa["hobi"] = "coding"
del siswa["kelas"]

for kunci, nilai in siswa.items():
    print(kunci, "->", nilai)

print("Kunci:", list(siswa.keys()))
print("Nilai:", list(siswa.values()))
print("Ada nama?", "nama" in siswa)
