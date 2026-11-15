class Rekening:
    def __init__(self, pemilik, saldo):
        self.pemilik = pemilik
        self.__saldo = saldo      # atribut private

    @property
    def saldo(self):
        return self.__saldo

    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah

    def tarik(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
        else:
            print("Saldo tidak cukup atau jumlah tidak valid")

rek = Rekening("Farhan", 100000)
rek.setor(50000)
rek.tarik(30000)
rek.tarik(999999)
print("Saldo sekarang:", rek.saldo)

try:
    print(rek.__saldo)
except AttributeError:
    print("Atribut __saldo tidak bisa diakses langsung dari luar class")
