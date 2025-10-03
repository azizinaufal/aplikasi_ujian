def halo():
    print("Hello")

halo()

def halo_nama(name):
    print("Hello " +  str(name))
halo_nama("azozo")

def hitung_luas_persegi_panjang(p,l):
    luas = p * l
    return luas

print(hitung_luas_persegi_panjang(5,10))

def cetak(*list):
    for item in list:
        print(item)
cetak(1,23,4,5,6)

def cetak_dict(**dict):
    for key, value in dict.items():
        print(f"{key}:{value}")

cetak_dict(nama="azizi",umur=25, kota="purwokerto")