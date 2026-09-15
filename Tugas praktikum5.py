buku = {
    "judul": "Pergi",
    "penulis": "Tere Liye",
    "tahun_terbit": 2018
}

while True:
    print("Menu:")
    print("1. Lihat buku")
    print("2. Tambah penerbit")
    print("3. Ubah penulis buku")
    print("4. Hapus penerbit")
    print("5. Tampilkan data setelah diubah")
    print("6. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        print("Lihat buku")
        print("Judul:", buku["judul"])
        print("Penulis:", buku["penulis"])
        print("Tahun Terbit:", buku["tahun_terbit"])

    elif pilih == "2":
        print("Tambah penerbit")
        penerbit_baru = input("Masukkan penerbit baru: ")
        buku["penerbit"] = penerbit_baru
        print("Penerbit buku berhasil ditambahkan")

    elif pilih == "3":
        print("Ubah penulis buku")
        penulis_baru = input("Masukkan penulis baru: ")
        buku["penulis"] = penulis_baru
        print("Penulis buku berhasil diubah")

    elif pilih == "4":
        print("Hapus penerbit")
        if "penerbit" in buku:
            del buku["penerbit"]
            print("Penerbit buku berhasil dihapus")
        else:
            print("Penerbit tidak ditemukan")

    elif pilih == "5":
        print("Tampilkan data setelah diubah")
        print("Judul:", buku["judul"])
        print("Penulis:", buku["penulis"])
        print("Tahun Terbit:", buku["tahun_terbit"])
        if "penerbit" in buku:
            print("Penerbit:", buku["penerbit"])

    elif pilih == "6":
        print("Terima kasih")
        break

    else:
        print("Pilihan tidak valid")