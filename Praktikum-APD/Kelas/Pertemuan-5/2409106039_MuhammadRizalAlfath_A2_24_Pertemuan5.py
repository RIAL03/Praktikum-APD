# nama = ["Celio", "Shandy", "Farel", "Ghazali", "Vito"]
# print(type(nama))

# #Cara memanggil list
# print(nama)
# print(nama[0])
# print(nama[2:5])

# #Menambahkan elemen di list
# print("Sebelum: ")
# print(nama)

# print("Sesudah: ")
# nama.append("Afrizal")
# print(nama)

# nama.insert(2,"Afrizal")
# print(nama)

# #Menimpa sebuah elemen pada list
# nama[4] = "Fufufafa"
# print(nama)

# #Mneghapus elemen list
# del nama[2]
# print(nama)

# hapus = nama.pop(2)
# print(nama)
# print(hapus)

# #Slicing list
# print(nama[0:2])

# #Penggunaan Step
# nama = ["Celio",
#         "Shandy",
#         "Farel",
#         "Ghazali",
#         "Vito",
#         "yuyun",
#         "adri",
#         "rizal",
#         "adi",
#         "ifnu"
# ]
# print("sebelum: ")
# print(nama)
# print("Sesudah: ")
# print(nama[1:9:2])

# #Menambahkan list
# matkul = ["apd", "apl", "basdat", "strukdat," ""]

# data = matkul + nama
# print(data)

# #Nested list
# data = ["farel", "celio", [1, 2]]
# print(data[2][1])

# data = ["farel", "celio", [1, 2, ["Hai", 23, 2.3]]]
# print(data[2][2][1])

# data = ["farel", "celio", [1, 2, ["Hai", 23, 2.3]]]
# print(data[2][2][::-1])

# #contoh lain ensted list
# matkul = [1, 2, 3, 4]
# print(matkul[3])

# matkul = [1, 2, 3, 4, [5, 6 ,7]]
# print(matkul[4])

# matkul = [1, 2, 3, 4, [5, 6 , 7, [8, 9, 10]]]
# print(matkul[4][3][::-1])

# #List menggunakan For looping
# matkul = [1, 2, 3, 4]
# for i in matkul:
#     print(i, end=' - ')
    
# matkul = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in matkul:
#     print(i)
        
# for i in matkul:
#     print(1)
#     for j in i:
#         print(j)

# #Tuple        
# nama = ("farel", "vito", "Shandy", "Rizal")
# print(nama[1:])

# nama = ("farel", "vito", "Shandy", "Rizal")
# absen, prodi, nim = nama
# print(absen)

print( 
"""
===========================
|   DATA MAHASISWA A24    |
===========================
|    1. TAMBAH DATA       |           
|    2. TAMPILKAN DATA    |          
|    3. UBAH DATA         |     
|    4. HAPUS DATA        |      
|    5. KELUAR            |  
===========================
"""
)

data_mahasiswa = []
while True:
    pilih = int(input("PILIH : "))
    if pilih == 1:
        nama = input("NAMA : ")
        nim = input("NIM : ")
        kelas = input("KELAS : ")
        data_mahasiswa.append([nama,nim,kelas])
    elif pilih == 2:
        for i in range(len(data_mahasiswa)):
            print(f"\n Data Mahasiswa ke-{i+1}\nNAMA : {data_mahasiswa[i][0]}\nNIM : {data_mahasiswa[i][1]}\nKELAS : {data_mahasiswa[i][2]}")
    elif pilih == 3:
        nama_lama = input("Nama Baru : ")
        for i in range(len(data_mahasiswa)):
            if data_mahasiswa[i][0] == nama_lama:
                nama_baru = input("NAMA : ")
                nim_baru = input("NIM : ")
                kelas_baru = input("KELAS : ")
                data_mahasiswa[i][0] = nama_baru
                data_mahasiswa[i][1] = nim_baru
                data_mahasiswa[i][2] = kelas_baru
    elif pilih == 4:
        nama_lama = input("Nama yang ingin dihapus")
        for i in range(len(data_mahasiswa)):
            if data_mahasiswa[i][0] == nama_lama:
                del data_mahasiswa[i]
    elif pilih == 5:
        print("Terima Kasih Telah Mengakses Data Mahasiswa")
        break
    else:
        print("Anda Salah Input")