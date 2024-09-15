nama = input("Masukan Nama Lengkap")
nim = input("Masukan Nim")
harga = int(input("Masukan Harga Beras"))

beras_mawar = harga - (harga * (11/100))
beras_sania = harga - (harga * (14/100)) 
beras_maknyus = harga - (harga * (17/100)) 

print(nama, "dengan NIM", nim, "ingin membeli beras seharga", harga, "\nJika dia membeli beras Mawar ia harus  membayar", beras_mawar, "Setelah mendapat diskon 11%.\nJika dia membeli beras Sania ia harus membayar", beras_sania, "Setelah mendapat diskon 14%.\nJika dia membeli beras Maknyus ia harus membayar", beras_maknyus, "Setelah mendapat diskon 17%.")