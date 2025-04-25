class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return len(self.items) == 0
    def Push(self, item):
        self.items.append(item)
    def Pop(self):
        return self.items.pop()
    def Peek(self):
        return self.items[len(self.items) - 1]
    def Size(self):
        return len(self.items)

class Queue:
    def __init__(self, UkuranMax):
        self.items = []
        self.UkuranMax = UkuranMax
    def isEmpty(self):
        return len(self.items) == 0
    def isFull(self):
        return len(self.items) >= self.UkuranMax
    def Enqueue(self, item):
        if not self.isFull():
            self.items.insert(0, item)
            return True
        return False
    def Dequeue(self):
        if not self.isEmpty():
            return self.items.pop()
        return None
    def Peek(self):
        if not self.isEmpty():
            return self.items[-1]
        return None
    def Size(self):
        return len(self.items)
    def ukuran_max(self):
        return self.UkuranMax

def Menu():
    PilihanData = input("Pilih yang akan digunakan (Queue/Stack): ").lower()
    if PilihanData == "queue":
        queue = Queue
    elif PilihanData == "stack":
        stack = Stack()
    else:
        print("pilihan anda tidak valid")
        return

    while True:
        if PilihanData == "stack":
            print("| Menu Aplikasi Stack |")
            print("===============================")
            print("1. Push Object")
            print("2. Pop Object")
            print("3. Cek Empty")
            print("4. Tampilkan Objek Terakhir")
            print("5. Tampilkan Panjang Dari Stack")
            print("6. Selesai")
            print("===============================")
        else:
            print("| Menu Aplikasi Queue |")
            print("==========================")
            print("1. input data")
            print("2. hapus data")
            print("3. cek data awal")
            print("4. cek ukuran maksimal")
            print("5. cek panjang data")
            print("6. cek apakah data kosong")
            print("7. cek apakah data penuh")
            print("8. selesai")
            print("==========================")

        try:
            pilihan = int(input("masukkan pilihan anda: "))
            if PilihanData == "stack":
                if pilihan == 1:
                    print("Halo, Selamat Datang Di Aplikasi Stack Kami!")
                    objek = str(input("objek yang ingin ditambahkan: "))
                    stack.Push(objek)
                    print(f"objek '{objek}' telah berhasil ditambahkan")
                elif pilihan == 2:
                    print(f"objek '{stack.Pop}' telah berhasil dihapus")
                elif pilihan == 3:
                    print(stack.isEmpty())
                elif pilihan == 4:
                    print("objek terakhir yang ditambahkan adalah " + stack.Peek())
                elif pilihan == 5:
                    print("panjang dari stack adalah " + str(stack.Size()))
                elif pilihan == 6:
                    print("terimakasih telah menggunakan aplikasi Stack kami!")
                    break
                else:
                    print()
            elif PilihanData == "queue":
                if pilihan == 1:
                    objek = input("data yang akan ditambahkan: ")
                    if queue.Enqueue(objek):
                        print("data" + objek + "berhasil ditambahkan")
                    else:
                        print("Queue penuh, tidak dapat menambahkan data!!")
                elif pilihan == 2:
                    data = queue.Dequeue()
                    if data is not None:
                        print("data" + data + "telah dihapus")
                    else:
                        print("Queue kosong, tidak ada yang bisa dihapus!!")
                elif pilihan == 3:
                    data = queue.Peek()
                    if data is not None:
                        print("data paling awal adalah:", data)
                    else:
                        print("Queue kosong, tidak ada data")
                elif pilihan == 4:
                    print("Ukuran Maksimal:", queue.ukuran_max())
                elif pilihan == 5:
                    print("panjang Queue adalah:", queue.Size())
                elif pilihan == 6:
                    print("apakah Queue kosong?", queue.isEmpty())
                elif pilihan == 7:
                    print("apakah Queue penuh?", queue.isFull())
                elif pilihan == 8:
                    print("terimakasih telah menggunakan aplikasi Queue kami!")
                    break
                else:
                    print()
        except ValueError:
            print("masukkan angka sesuai menu, pilihan anda tidak valid")
        print()

if __name__ == "__main__":
    Menu()