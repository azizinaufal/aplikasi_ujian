nama = "Budi"
umur = 25

pesan = "Nama saya " + nama +" Dengan Umur "+ str(umur)
print(pesan)

print(len(pesan))

print(nama[0:3])

nama = "Alice"
print(nama)
print(nama.upper())
print(nama.lower())
nama_capital = nama.capitalize()
print(nama_capital)
print(nama.title())

nama= "Mohamad naufal Azizi"
print(nama.strip())
print(nama.replace("naufal","Naufal"))

kalimat = "Baris pertama\nBaris Kedua"
print(kalimat)
kalimat="\tMohamad Naufal Azizi"
print(kalimat)
path= "C:\\Users\\ASUS\\PycharmProjects"
print(path)
kalimat = "\rDIa berkata \"Hello\" kepada saya"
print(kalimat)

nama = "Azizi"
umur = 22
kota = "Purwokerto"
kalimat =f"Halo nama saya {nama} berumur {umur} dari Kota {kota}"
print(kalimat)

harga = 10000
jumlah = 3
total = f"Total: {harga*jumlah}"
print(total)
kalimat = f"Halo {nama.upper()}"
print(kalimat)