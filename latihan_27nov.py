 # A. Membuat list penumpang awal
penumpang = ["William", "Kate", "Anderson", "Jame", "Mady"]
print("A. List penumpang awal:", penumpang)

# B. Menambahkan Jones pada posisi terakhir
penumpang.append("Jones")
print("B. Setelah Jones bergabung:", penumpang)

# C. Anderson digantikan oleh Grace
penumpang[2] = "Grace"
print("C. Setelah Anderson digantikan Grace:", penumpang)

# D. Memeriksa apakah Thompson ada dalam list
print  ("D. apakah nama Thompson ada dalam list:", "Thompson" in penumpang)

# E. Mengurutkan nama sesuai abjad
penumpang.sort()
print ("E. urutan nama:", penumpang)

# F. Menampilkan semua penumpang menggunakan perulangan
print("F. Daftar semua penumpang:")
for nama in penumpang:
    print(nama)

# G. mengosongkan list setelah semua penumpang turun
penumpang.clear()
print("G. List setelah semua penumpang turun:", penumpang)
