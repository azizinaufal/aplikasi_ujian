# print("Program Pencatatan nilai")
# file = open("nilai_siswa.txt", "w")
#
# while True:
#     nama = input("Nama Siswa: (enter untuk selesai)")
#     if nama=="":
#         break
#
#     nilai = input("Nilai Siswa: )")
#
#     file.write(f"Nama: {nama}, Nilai :{nilai}\n")
#     print("Data nama berhasil disimpan")
# file.close()
# print("Program selesai")

print("Menampilkan data nilai")
try:
    with open("nilai_siswa.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            print(data[0], ":", data[1])
except FileNotFoundError:
    print("File tidak ditemukan")

# file.close()
print("program selesai")