from collections import deque

class Barang:
    def __init__(self, nama, harga, jumlah):
        self.nama = nama
        self.harga = harga
        self.jumlah = jumlah

    def total(self):
        return self.harga * self.jumlah

def tambah_barang(daftar):
    nama = input("Masukkan nama barang (Enter jika tidak ada barang): ")
    if nama == '':
        return False
    try:
        jumlah = int(input(f"Jumlah Barang '{nama}': "))
        harga = int(input(f"Harga Barang '{nama}': Rp "))
        barang = Barang(nama, harga, jumlah)
        daftar.append(barang)
    except ValueError:
        print("Input jumlah dan harga harus angka!!")
    return True

def tampilkan_daftar(daftar):
    if not daftar:
        print("Belum ada barang yang dimasukkan")
        return
    print("\nDaftar Belanja:")
    print(f"{'Nama Barang':<20}{'Jumlah Barang':<20}{'Harga Barang':<20}{'Total':<15}")
    print("-" * 50)
    for item in daftar:
        print(f"{item.nama:<20}{item.jumlah:<20}{item.harga:<20}{item.total():<15}")
    print("-" * 50)

def total_belanja(daftar):
    return sum(item.total() for item in daftar)

antrian = deque()

jumlah_pelanggan = int(input("Jumlah pelanggan hari ini: "))
for i in range(jumlah_pelanggan):
    nama = input(f"Nama pelanggan ke-{i+1}: ")
    antrian.append(nama)

while antrian:
    pelanggan = antrian.popleft()
    print(f"\n=== TRANSAKSI PELANGGAN {pelanggan.upper()} ===")
    daftar_belanja = []

    while True:
        print("\nMenu Minimarket Tetangga:")
        print("1. Tambah Barang")
        print("2. Lihat Daftar")
        print("3. Total Keseluruhan & Akhiri Daftar Belanja")
        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == '1':
            if not tambah_barang(daftar_belanja):
                print("Tidak ada barang ditambahkan.")
        elif pilihan == '2':
            tampilkan_daftar(daftar_belanja)
        elif pilihan == '3':
            tampilkan_daftar(daftar_belanja)
            total = total_belanja(daftar_belanja)
            print(f"Total belanja: Rp {total:,.0f}")
            while True:
                try:
                    bayar = int(input("Jumlah bayar: Rp "))
                    if bayar < total:
                        print("Uang tidak cukup. Masukkan jumlah yang cukup!")
                    else:
                        kembalian = bayar - total
                        print(f"Kembalian: Rp {kembalian:,.0f}")
                        print(f"Transaksi {pelanggan} selesai.\n")
                        break
                except ValueError:
                    print("Masukkan angka yang valid!")
            break
        else:
            print("Pilihan tidak valid, Coba lagi!")

print("Semua pelanggan telah dilayani!!")
print("Terimakasih telah berbelanja di Minimarket Tetangga!!")