def ekstrasi_data():
    """
    Tanggal     : 18 Maret 2023,
    waktu       : 02:38:00 WIB
    Magnitudo   : 5.1
    Kedalaman   : 91 km
    Lokasi      : LS=5.90  BT=125.99
    Pusat Gempa : 224 km BaratLaut MELONGUANE-SULUT
    keterangan  : tidak berpotensi TSUNAMI
    :return:
    """
    hasil = dict ()
    hasil["tanggal"] = "18 Maret 2023"
    hasil["waktu"] = "02:38:00 WIB"
    hasil["magnitudo"] = 5.1
    hasil["kedalaman"] = "91 km"
    hasil["lokasi"] = {'ls':5.90, 'bt':125.99}
    hasil["pusat gempa"] = "224 km BaratLaut MELONGUANE-SULUT"
    hasil["keterangan"] = "tidak berpotensi TSUNAMI"

    return  hasil
def tampilkan_data(result):
    print("Gempa Terakhir beradasarkan BMKG ")
    print(f"Tanggal,{result['tanggal']}")
    print(f"waktu,{result['waktu']}")
    print(f"magnitudo,{result['magnitudo']}")
    print(f"kedalaman,{result['kedalaman']}")
    print(f"lokasi: LS={result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print(f"pusat gempa,{result['pusat gempa']}")
    print(f"keterangan,{result['keterangan']}")

# if __name__ == '__main__':
#     print("ini adalah pckage gempa terkini")