def tambah_barang(daftar):
    nama = input("Masukkan nama barang(enter jika tidak ada barang): ")
    if nama == '':
        return False
    try:
        jumlah = int(input(f"Jumlah barang '{nama}': "))
        harga = int(input(f"Harga barang '{nama}'  : Rp "))
        from barangUTS import Barang
        barang = Barang(nama, harga, jumlah)
        daftar.append(barang)
    except ValueError:
        print("Input jumlah dan harga harus angka!!")
    return True

def tampilkan_daftar(daftar):
    if not daftar:
        print("Belum ada barang yang dimasukkan :(")
        return
    print("===DAFTAR BELANJA==")
    print(f"{'Nama barang':<20}{'Jumlah barang':<20}{'Harga barang':<20}{'Total':<20}")
    print('-' * 80)
    for item in daftar:
        print(f"{item.nama:<20}{item.jumlah:<20}{item.harga:<20}{item.total():<20,.0f}")
    print('-' * 80)

def total_belanja(daftar):
    return sum(item.total() for item in daftar)