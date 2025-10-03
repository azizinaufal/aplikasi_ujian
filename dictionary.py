siswa = {
"nama" : "Azizi",
"umur" : 22,
"kelas" : "Fresh Grad"
}
print(siswa)

print(siswa["nama"])
print(siswa["kelas"])

siswa["kelas"] = "1 year exp"
print(siswa)

for key in siswa:
    print(key, siswa[key])

for key, value in siswa.items():
    print(key, value)