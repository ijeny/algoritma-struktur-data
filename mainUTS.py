from collections import deque
import belanjaUTS

antrian = deque()

Jumlahpelanggan = int(input("Jumlah pelanggan hari ini: "))
for i in range(Jumlahpelanggan):
    nama = input(f"Nama pelanggan ke-{i+1}: ")
    antrian.append(nama)

while antrian:
    pelanggan = antrian.popleft()
    print(f"=== TRANSAKSI PELANGGAN {pelanggan.upper()} ===")
    daftarBelanja = []

    while True:
        print("----- Menu Minimarket Tetangga -----")
        print("1. Tambah barang")
        print("2. Lihat daftar")
        print("3. Total keseluruhan & Akhiri daftar belanja")
        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == '1':
            if not belanjaUTS.tambah_barang(daftarBelanja):
                print("Tidak ada barang yang ditambahkan.")
        elif pilihan == '2':
            belanjaUTS.tampilkan_daftar(daftarBelanja)
        elif pilihan == '3':
            belanjaUTS.tampilkan_daftar(daftarBelanja)
            total = belanjaUTS.total_belanja(daftarBelanja)
            print(f"Total belanja: Rp{total:,.0f}")
            while True:
                try:
                    bayar = int(input("Jumlah Pembayaran: Rp"))
                    if bayar < total:
                        print("Uang anda tidak cukup. Masukkan kembali pembayaran anda!!")
                    else:
                        kembalian = bayar - total
                        print(f"Kembalian: Rp{kembalian:,.0f}")
                        print(f"Transaksi anda telah selesai!")
                        break
                except ValueError:
                    print("Masukkan angka yang valid!!")
            break
        else:
            print("Pilihan tidak valid, coba lagi!!")

print("\n====================================================")
print("Semua pelanggan telah dilayani.")
print("Terimakasih telah berbelanja di Minimarket Tetangga!!")