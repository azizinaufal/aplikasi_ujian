from itertools import count

daftar_kosong = []

angka = [1,2,3,4,5]
print(angka)

nama = ["Mohamad","naufal","Azizi"]
print(nama)

campuran = [1,"Mohamad", 2, "Naufal"]
print(campuran)



warna = ["merah","kuning", "hijau"]
print(warna)
warna[1] = "biru"
print(warna)

buah = ["apple", "mangga"]
print(buah)
buah.append("durian")
print(buah)
buah.insert(1,"kedelai")
print(buah)
buah.remove("mangga")
print(buah)
buah.pop()
print(buah)
del buah[0]
print(buah)

buah = ["apple", "jeruk", "mangga"]
print(len(buah))

satu = [1,2,3,4,5]
dua = [6,7,8,9]
gabungan = satu + dua
print(gabungan.count(1))
print(gabungan)
banyak_buah = ["apple", "jeruk", "mangga", "durian"]
for item in banyak_buah:
    print(item)
if "apple" in banyak_buah:
    print("ada apple")
else:
    print("tidak ada apple")