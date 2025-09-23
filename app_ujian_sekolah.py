import random
def ambil_soal():
    soal_asli = []
    try:
        with open("bank_soal.txt","r") as file:
            for line in file:
                soal_asli.append(line.strip())
            return soal_asli
    except FileNotFoundError:
        print("FIle tidak ditemukan")
soal_asli = ambil_soal()


def buat_soal():
    soal_ujian=[]
    #acaksoal
    random.shuffle(soal_asli)
    
    for i in range(10):
        soal = soal_asli[i]
        data = soal.split("|")
        pertanyaan = data[0]
        jawaban_semua=data[1]

        jawaban = jawaban_semua.split(",")
        jawaban_benar = jawaban[0]

        random.shuffle(jawaban)

        soal_ujian.append({
           "pertanyaan" : pertanyaan,
           "jawaban" : jawaban,
           "jawaban_benar" : jawaban_benar
       }) 
    return soal_ujian

def app_ujian():
    soal_ujian = buat_soal()
    opsi = ["A","B","C","D"]

    jawaban_benar = 0
    jawaban_salah = 0
    for i in range(len(soal_ujian)):
        soal = soal_ujian[i]
        print("Pertanyaan", i+1,":", soal["pertanyaan"])
        print("Jawaban: " )
        for j in range(len(soal["jawaban"])):
            jawaban = soal["jawaban"][j]
            print(opsi[j] ,"." , jawaban)

        jawaban_user = input("Pilih Jawaban (A/B/C/D): ")
        jawaban_user_index = opsi.index(jawaban_user)
        jawaban_asli_user = soal["jawaban"][jawaban_user_index]

        if jawaban_asli_user == soal["jawaban_benar"]:
            print("Jawaban benar")
            jawaban_benar +=1
        else:
            print("Jawaban Salah")
            jawaban_salah +=1
    print("Hasil Ujian")
    print("Jawaban Benar", jawaban_benar)
    print("Jawaban Salah", jawaban_salah)
    print("Hasil nilai ujian", jawaban_benar/(jawaban_benar+jawaban_salah) *100, "%")
app_ujian()




    