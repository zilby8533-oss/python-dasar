from abc import ABC, abstractmethod

class Pembayaran(ABC):
    @abstractmethod
    def bayar(self, jumlah):
        pass

class Tunai(Pembayaran):
    def bayar(self, jumlah):
        return f"Bayar tunai Rp{jumlah:,}"

class Transfer(Pembayaran):
    def bayar(self, jumlah):
        return f"Bayar transfer bank Rp{jumlah:,}"

for metode in [Tunai(), Transfer()]:
    print(metode.bayar(150000))

try:
    Pembayaran()
except TypeError as e:
    print("Abstract class tidak bisa dibuat object:", e)
