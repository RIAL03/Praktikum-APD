nama = input("Masukan Nama")
nim = input("masukan Nim")
tahun = input("Masukan Lama Cicilan")
pinjaman = int(input("Masukan Pinjaman"))

if tahun == "1" or tahun == "2" or tahun == "3" :
  if tahun == "1" :
    bungaPerbulan = ((7 / 100) / 12) * pinjaman 
    cicilanPerbulan = (pinjaman + bungaPerbulan) / 12
 
  elif tahun == "2" :
    bungaPerbulan = ((13 / 100) / 12) * pinjaman 
    cicilanPerbulan = (pinjaman + bungaPerbulan) / 24

  elif tahun == "3" :
    bungaPerbulan = ((19 / 100) / 12) * pinjaman 
    cicilanPerbulan = (pinjaman + bungaPerbulan) / 36

  print(f"{nama} dengan nim {nim} ingin meminjam uang di Bank sebanyak {pinjaman} dengan pengembalian secara kredit.\nJika lama cicilan {tahun} tahun, dia harus membayar cicilan sebesar Rp {cicilanPerbulan} per bulan")

else :
  print("Kondisi Ga Memenuhi Syarat, Coba di lebih teliti")