#===========================÷=
print("="*20)
ulang = 10
for i in range(ulang):
  print(f"perulangan ke- {i}")
 
#===========================÷= 
print(" ")
print("="*20)
for j in range(12):
  print("Hello")
print("hai")

#===========================÷=
print(" ")
print("="*20)
simpan = [12, "udin petot", 14.5, True, "A"]
for i in simpan:
  print(i)
 
#===========================÷=
print(" ")
print("="*20) 
print("Menu Rumah Makan Informatika")
makan = ["nasi goreng", "mie ayam", "mie goreng", "bakso", "soto"]
for i in makan:
  print(i)

#===========================÷=  
print(" ")
print("="*20) 
print("Menu Rumah Makan Informatika")
makan = ["nasi goreng", "mie ayam", "mie goreng", "bakso", "soto"]
for i, menu in enumerate(makan,start=1):
  print(f"{i}.{menu}")

#===========================÷=    
print(" ")
print("="*20) 
print("Menu Rumah Makan Informatika")
makan = ["nasi goreng", "mie ayam", "mie goreng", "bakso", "soto"]
for i in range(len(makan)):
  print(f"{i+1}.{makan[i]}")
  
#===========================÷=    
print(" ")
print("="*20) 
for i in range(1,4):
  for j in range(1,4):
    print(f"{i} x {j} = {i * j}")
  print(f"\n \n")

#===========================÷=    
print(" ")
print("="*20) 
makanan = ["mie", "sop", "bakso"]
minuman = ["es teh", "air putih", "es jeruk"]
for i in makanan:
  for j in minuman:
    print(f"{i} & {j}")
  print(f"\n \n")
  
#===========================÷=    
print(" ")
print("="*20)
while True:
  print("Hello world")
  break

#===========================÷=    
print(" ")
print("="*20)  
jawab = "ya"
hitung = 0
while(jawab == "ya"):
  hitung += 1
  break #boleh dihapus
  jawab = input("ulang lagi tidak? ")
  print(f"Total pengulangan: {hitung}")
  
#===========================÷=    
print(" ")
print("="*20)  
i = 0
while i < 5:
  print(i)
  i+=1
  
#===========================÷=    
print(" ")
print("="*20)    
hitung = 0
while True:
  hitung += 1
  break #boleh dihapus
  ulang = input("Masih ingin lanjut? ")
  if ulang == "y" or ulang == "Y":
    print("Oke Kita lanjut")
    continue
print(f"total pengulangan: {hitung}")

#===========================÷=    
print(" ")
print("="*20)  
print("Daftar bilangan ganjil dari 1-10")
for i in range(10):
  if i % 2 == 0:
    continue
    print("genap")
  else:
    print("ganjil")
    continue

#Studi Kasus 
#===========================÷=    
print(" ")
print("="*20)  
total = 0
while True:
  angka = int(input("Masukan Bilangan Positif"))
  if angka < 0:
    break
  total += angka
print("jumlah total adalah:",angka)

# Meminta input dari pengguna untuk range maksimal
#range_maksimal = int(input("Masukkan range maksimal: "))

# Inisialisasi variabel untuk menyimpan jumlah bilangan prima
#hitung_prima = 0

# Loop untuk memeriksa setiap angka dari 1 hingga range_maksimal
#for angka in range(1, range_maksimal):
#  angka += 1
#  apakah_prima = True  # Anggap angka tersebut prima

    # Cek apakah angka memiliki pembagi selain 1 dan dirinya sendiri
#  for i in range(2, angka):
#    if angka % i == 0:
#      apakah_prima = False  # Jika ada #pembagi, bukan bilangan prima
          # print(f"{angka} bukan prima")
#      break
    # Jika angka tersebut prima, tambahkan jumlah hitung_prima
#    if apakah_prima == True:
#      print(f"{angka} prima")
#     hitung_prima += 1
        
# output
#print(f"Jumlah bilangan prima antara 1 hingga {range_maksimal} adalah: {hitung_prima}")