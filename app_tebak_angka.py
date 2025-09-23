import random
def app_tebak():

    angka_acak = random.randint(1, 10)
    print("Maksimal Tebakan adalah 3")
    counter = 0
    max = 3
    while counter < max:
        counter +=1
        try:
            tebakan = int(input(f"Masukan Tebakan Anda: "))
        except ValueError:
            print("Angka yang dimasukan tidak valid")
        if tebakan < angka_acak:
            print("Angka terlalu kecil")
        elif tebakan > angka_acak:
            print("Angka terlalu besar")
        elif tebakan == angka_acak:
            print(f"Angka tebakan anda benar, yaitu {angka_acak}")
            break
    else:
        print("Anda sudah melewati batas tebaakan")
        print(f"Angka tebakan salah, yang benar adalah  {angka_acak}")



def app_menu():
    while True:
        print("=== Permainan Tebak Angka ===")
        print("1.Tebak Angka")
        print("2.Keluar")
        print("=== Permainan Tebak Angka ===")
        try:
            pilihan = int(input("pilihan : "))
        except ValueError:
            print("Angka yang dimasukan tidak valid")
        if pilihan == 1:
            app_tebak()
        elif pilihan == 2:
            print("Sampai jumpa")
            break
        else:
            print("Pilihan tidak valid")
app_menu()