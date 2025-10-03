# print("=========KAlkulator sederhana===========")

# try:
#     angka1 = int(input("angka1: "))
#     angka2 = int(input("angka2: "))
#     hasil = angka1 / angka2
#     print("Hasil: ", hasil)
# except ValueError:
#     print("input pengguna bukan error")
# except ZeroDivisionError:
#     print("tidak bisa dibagi 0")
# except:
#     print("Terjadi kesalahan dalam program")
#
# print("Priogram End")

try:
    angka = int(input("Masukan Angka"))
except ValueError:
    print("Angka tidak valid")
else:
    print(f"Angka yang anda masukan: {angka}")
    if angka < 0:
        print("Angka positif")
    elif angka > 0:
        print("Angka negatif")
    else:
        print("Angka 0")
finally:
    print("Program selesai")