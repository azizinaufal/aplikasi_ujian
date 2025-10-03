from xml.dom.minidom import ProcessingInstruction


def app_penjumlahan():
    try:
        angka1 = int(input("angka 1: "))
        angka2 = int(input("angka 2: "))
        hasil = angka1 + angka2
        print(f"Hasil penjumalah: {hasil}")
        print("Program penjumalahn selesai")
    except ValueError:
        print("Angka yang dimasukan tidak valid")

def app_pengurangan():
    try:
        angka1 = int(input("angka 1: "))
        angka2 = int(input("angka 2: "))
        hasil = angka1 - angka2
        print(f"Hasil pengurangan: {hasil}")
        print("Program pengurangan selesai")
    except ValueError:
        print("Angka yang dimasukan tidak valid")
def app_perkalian():
    try:
        angka1 = int(input("angka 1: "))
        angka2 = int(input("angka 2: "))
        hasil = angka1 * angka2
        print(f"Hasil perkalian: {hasil}")
        print("Program perkalian selesai")
    except ValueError:
        print("Angka yang dimasukan tidak valid")
def app_pembagian():
    try:
        angka1 = int(input("angka 1: "))
        angka2 = int(input("angka 2: "))
        hasil = angka1 / angka2
        print(f"Hasil pembagian: {hasil}")
        print("Program pembagian selesai")
    except ValueError:
        print("Angka yang dimasukan tidak valid")
def app_menu():
    while True:
        print("=== Program kalkulator sederhana ===")
        print("1. Penjumalahn")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. tutup")
        print("=== Program kalkulator sederhana ===")
        try:
            pilihan = int(input("pilihan : "))
        except ValueError:
            print("Angka yang dimasukan tidak valid")
        if pilihan == 1:
            app_penjumlahan()
        elif pilihan == 2:
            app_pengurangan()
        elif pilihan == 3:
            app_perkalian()
        elif pilihan == 4:
            app_pembagian()
        elif pilihan == 5:
            print("sampai jumpa lagi")
            break
app_menu()