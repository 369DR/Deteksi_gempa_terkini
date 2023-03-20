"""
Aplikasi deteksi gempa terkini
MODULARISASI dengan FUNGTION
MODULARISASI dengan PACKAGE
"""
import  gempaterbaru

if __name__ == '__main__':
    print("Aplikasi utama")
    result = gempaterbaru.ekstrasi_data()
    gempaterbaru.tampilkan_data(result)