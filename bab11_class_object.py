class Siswa:
    sekolah = "SMK Contoh"

    def __init__(self, nama, kelas):
        self.nama = nama
        self.kelas = kelas

    def perkenalan(self):
        return f"Saya {self.nama}, kelas {self.kelas}, sekolah di {self.sekolah}"

siswa1 = Siswa("Farhan", "XI")
siswa2 = Siswa("Budi", "XII")
print(siswa1.perkenalan())
print(siswa2.perkenalan())
siswa2.kelas = "XI"
print("Setelah diubah:", siswa2.perkenalan())
