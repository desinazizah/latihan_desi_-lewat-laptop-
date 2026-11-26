# a. Membuat 2 set untuk hari pertama dan hari kedua
hari_pertama = {"keju", "tepung", "garam", "gula", "coklat"}
hari_kedua = {"garam", "gula", "coklat", "kecap"}

# b. Tambahkan "keju" pada pembelian hari kedua
hari_kedua.add("keju")

# e. Hapus "garam" pada pembelian hari pertama
hari_pertama.discard("garam")

# c. Barang yang sama pada hari pertama dan hari kedua
print("Barang yang sama di kedua hari:", hari_pertama.intersection(hari_kedua))

# d. Barang di hari pertama tapi tidak di hari kedua
print("Hanya ada di hari pertama:", hari_pertama.difference(hari_kedua))

# f. Barang di hari kedua tapi tidak di hari pertama
print("Hanya ada di hari kedua:", hari_kedua.difference(hari_pertama))

# g. Barang yang tidak sama (unik di masing-masing hari)
print("Barang yang tidak sama:", hari_pertama.symmetric_difference(hari_kedua))

# h & i. Tampilkan semua keperluan akhir
print("Keperluan akhir hari pertama:", hari_pertama)
print("Keperluan akhir hari kedua  :", hari_kedua)