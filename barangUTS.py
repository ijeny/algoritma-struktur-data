class Barang:
    def __init__(self, namaBarang, hargaBarang, jumlahBarang):
        self.nama = namaBarang
        self.jumlah = jumlahBarang
        self.harga= hargaBarang

    def total(self):
        return self.harga * self.jumlah