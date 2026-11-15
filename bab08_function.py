def sapa(nama, sapaan="Halo"):
    return f"{sapaan}, {nama}!"

def jumlah(*angka):
    return sum(angka)

def profil(**data):
    for kunci, nilai in data.items():
        print(kunci, ":", nilai)

kuadrat = lambda n: n ** 2

print(sapa("Farhan"))
print(sapa("Farhan", sapaan="Selamat pagi"))
print("Jumlah:", jumlah(1, 2, 3, 4, 5))
profil(nama="Farhan", kelas="XI", hobi="coding")
print("Kuadrat 9:", kuadrat(9))
