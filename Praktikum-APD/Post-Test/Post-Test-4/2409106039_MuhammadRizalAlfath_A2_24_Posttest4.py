# Untuk Username dan password
# Username : rizal
# Password : 39

truee = True
# Kondisi looping jika user mau mengulang
while truee:
  print("Silahkan Login Dulu :")
  for i in range(2,-1,-1):
    username = input("Masukan Username : ( rizal )")
    password = input("Masukan Password : ( 39 )")
   
    if username == "rizal" and password == "39":
      print(f"Hello {username} Login Berhasil")
      
      isi = True
      jawaban = True
      # Kondisi Berhasil login
      while isi :
       # Melanjutkan program menghitung Pinjaman
        if isi == True and jawaban == True:
          nama = input("Masukan Nama :")
          nim = input("Masukan Nim :")
          tahun = input("Masukan Lama Cicilan :")
          pinjaman = int(input("Masukan jumlah Pinjaman :"))
          
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
          
        isii = input("Ngulang isi? : (y / n)")
        #Kondisi mau mengulang atau tidak 
        if isii == "y":
          jawaban = True
        elif isii == "n":
          isi = False
          truee = False
        else :
          print("Input salah, Pilihan hanya : (y / n)")
          jawaban = False
      break
   
    # Kondisi Username / Password Salah
    else :
      print(f"Username atau Password salah\nSilahkan coba lagi, Sisa Percobaan {i}")
      if i == 0:
        print("Maaf Percobaan Anda Habis, Silahkan Coba lagi nanti")
        truee = False
print("Terima Kasih")