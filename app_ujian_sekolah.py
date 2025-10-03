def ambil_soal():
    with open("bank_soal.txt", "r") as file:
        bank_soal = []
        for line in file:
            bank_soal.append(line.strip())
    return bank_soal

def buat_soal():
    soal_asli = []
    semua_soal=ambil_soal()
    for line in semua_soal:
        data = line.split("|")
        soal_ujian = data[0]

        jawaban = data[1]
        semua_jawaban = jawaban.split(",")
        jawaban_benar = semua_jawaban[0]

        soal_asli.append({
        "soal_ujian":soal_ujian,
        "jawaban":jawaban,
        "jawaban_benar":jawaban_benar
        })
    return soal_asli

def app_ujian():
    soal = buat_soal()
    for i in range(10):
        data_soal = soal[i]
        soal_ujian = data_soal["soal_ujian"]
        jawaban_ujian = data_soal["jawaban"].split(",")
        print(soal_ujian)
        for j in range(len(jawaban_ujian)):
            data_soal = jawaban_ujian[j]
            print(data_soal)



app_ujian()