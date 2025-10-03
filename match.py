hari = str(input("Masukan Nama hari: "))

match hari:
    case "senin" | "selasa" | "rabu" | "kamis" | "jum'at":
        print("Hari Kerja")
    case "sabtu" | "minggu":
        print("Hari libur")
    case _:
        print("Hari tikda ditemukan")
