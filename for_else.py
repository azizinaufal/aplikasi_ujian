kata = input("Masukan kata: ")
huruf = input("Masukan huruf: ")

for x in kata:
    if huruf == x:
        print(f"Huruf {huruf} ada di dalam kata {kata}")
        break
else:
    print(f"Huruf {huruf} tidak ditemukan dalam kata {kata}")