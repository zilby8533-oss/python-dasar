class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def bersuara(self):
        return "..."

class Kucing(Hewan):
    def bersuara(self):
        return "Meong"

class Anjing(Hewan):
    def __init__(self, nama, ras):
        super().__init__(nama)
        self.ras = ras

    def bersuara(self):
        return "Guk guk"

    def jaga_rumah(self):
        return f"{self.nama} sedang menjaga rumah"

kucing = Kucing("Tom")
anjing = Anjing("Rex", "Husky")
print(kucing.nama, "->", kucing.bersuara())
print(anjing.nama, f"({anjing.ras}) ->", anjing.bersuara())
print(anjing.jaga_rumah())
