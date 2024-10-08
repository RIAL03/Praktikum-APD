# fitur = int(input("pilih fitur : "))
# match fitur :
#     case 1:
#         a = int(input("Masukkan angka 1 : "))
#         b = int(input("Masukkan angka 2 : "))
#         c = a + b 
#         print (f"hasil penjumlahan angka 1 dan angka 2 adalah {c}")
#     case 2:
#         a = int(input("Masukkan angka 1 : "))
#         b = int(input("Masukkan angka 2 : "))
#         c = a - b 
#         print (f"hasil pengurangan angka 1 dan angka 2 adalah {c}")
#     case 3:
#         a = int(input("Masukkan angka 1 : "))
#         b = int(input("Masukkan angka 2 : "))
#         c = a * b 
#         print (f"hasil perkalian angka 1 dan angka 2 adalah {c}")
#     case 4:
#         a = int(input("Masukkan angka 1 : "))
#         b = int(input("Masukkan angka 2 : "))
#         c = a / b 
#         print (f"hasil pembagian angka 1 dan angka 2 adalah {c}")


# buku = int(input("Masukkan jumlah buku = "))
# harga = int(input("Masukkan total harga buku = "))
# diskon = 0.20
# total_harga = buku * harga


# if buku >= 5 and total_harga > 100000:
#     diskon_barang = total_harga * diskon
#     harga_diskon = total_harga - diskon_barang
#     print(f"diskon yang diterima sebanyak {diskon_barang:.0f}")
#     print(f"Anda harus membayar sebanyak {harga_diskon:.0f} setelah mendapat diskon 20%")
# else: print("anda tidak mendapat diskon")

jenis_kelamin = input("Masukkan jenis kelamin anda (L/P) :")

hasil = "Jenis Kelamin Laki-Laki" if jenis_kelamin == "L" else "Jenis Kelamin Perempuan" if jenis_kelamin == "P" else "Jenis Kelamin Tidak Diketahui"

print(hasil)

Nilai = int(input("Masukkan Nilai anda"))
if Nilai > 100 :
    print("kondisi tidak memenuhi syarat")
if Nilai >= 80 : 
    if Nilai >= 90 and Nilai <= 100 :
      print("Nilai anda A+")
    if Nilai >= 80 and Nilai <= 89 :
      print("Nilai anda A-")
if Nilai >= 70 : 
    if Nilai >= 75 and Nilai <= 79 :
      print("Nilai anda B+")
    if Nilai >= 70 and Nilai <= 74 :
      print("Nilai anda B-")
else :
    print("kondisi tidak memenuhi syarat")