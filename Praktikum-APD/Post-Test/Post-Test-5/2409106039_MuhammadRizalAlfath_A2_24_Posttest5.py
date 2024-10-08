# Untuk Login Menjadi Admin
# Username = rizal
# Password = 039

admin = [["rizal","039"]]
user = []

characters = []
statistiks = []

program = True
while program:
    ulang1 = True
    while ulang1 :
        print("\n===== Selamat Datang Silahkan Login Dulu ======")
        print("silahkan pilih :")
        print("1. login sebagai admin")
        print("2. login sebagai user")
        print("3. register")
        print("4. keluar")
        print("================================================")
        
        login = input("Masukan Pilihan 1-4 :")

        # Login Sebagai Admin and User 
        if login == "1" or login == "2": 
            ulang = True
            while ulang:
                login_admin = input("Masukan username :")
                password_admin = input("Masukan Password :")
                if login == "1":
                    admins = [login_admin,password_admin]
                    users = []
                elif login == "2":   
                    users = [login_admin,password_admin]  
                    admins = []   
                if admins in admin or users in user:
                    if login == "1":
                        print("\nAnda Berhasil Login Sebagai admin")
                        akses = True
                    elif login == "2":
                        print("\nLogin Berhasil Sebagai User") 
                        akses = False                 
                    ulang1 = False
                    break
                elif admins not in admin or users not in user:
                        print("\nUsername / password salah")
                        while ulang:
                            print("1. Ulang Isi")
                            print("2. Keluar")
                            ulang = input("Pilih :")
                            if ulang == "1":
                                ulang = True
                                break
                            elif ulang == "2":
                                ulang = False
                            else:
                                print("\nPilihan hanya 1-2")
        
        elif login == "3":
            login_user = input("Masukan username: ").lower()
            password_user = input("Masukan Password: ")
                   
            # Cek duplikasi username
            while any(login_user == user[i][0] for i in range(len(user))):
                print(f"Username '{login_user}' sudah ada, masukkan Username Baru.")
                login_user = input("Username Baru: ").lower()    
                  
            users = [login_user, password_user]
            user.append(users)
            print("\nRegister Berhasil")
    
        elif login == "4":
            program = False
            ulang1 = False
            break
    
    # Program Managemen Statistik Character Game Rpg        
    while program:
        if akses == True:
            print("\n==== Manajemen Statistik Character ====")
            print("1. Tampilkan Character")
            print("2. Tambah Character")
            print("3. Edit Character")
            print("4. Hapus Character")
            print("5. Keluar")
            pilihan = input("Pilih 1-5 :")

            if pilihan == "1":
                if not characters:
                    print("\nCharacter Belum Ada")
                else :
                    for i in range(0,len(characters)):
                        print(f"\n======== Character {i + 1} ========")
                        print(f"Nama : {characters[i][0]}")
                        print(f"Role : {characters[i][1]}")
                        print(f"Ras : {characters[i][2]}")
                        print(f"\nStatistik :")
                        print(f"Hp : {statistiks[i][0]}")
                        print(f"MP : {statistiks[i][1]}")
                        print(f"Def : {statistiks[i][2]}")
                        print(f"Str : {statistiks[i][3]}")
                        print(f"Agi : {statistiks[i][4]}")
                        print(f"Int : {statistiks[i][5]}")
                        print(f"===============================")
                    
            elif pilihan == "2":
                print("\nMembuat Character baru")
                nama = input("Nama Character :").lower()
                
                # Cek duplikasi nama sebelum melanjutkan
                while any(nama == character[0] for character in characters):
                    print(f"Character Dengan Nama '{nama}' Sudah ada, masukan nama baru.")
                    nama = input("Nama Character :").lower()

                while True:
                    print("\n===== Role Character =====")  
                    print("1. Warrior        3. Priest")
                    print("2. Wizard         4. Paladin")     
                    role = input("\nRole Character (1-4) :")
                    if role == "1":
                        role = "warrior"
                        break
                    elif role == "2":
                        role = "wizard"
                        break
                    elif role == "3":
                        role = "priest"
                        break
                    elif role == "4":
                        role = "paladin"
                        break
                    else:
                        print("Pilihan invalid, pilihan hanya (1-4)")

                while True:            
                    print("\n===== Ras Character =====")
                    print("1. Human         3. Elf")
                    print("2. Dwarf         4. Orc")        
                    ras = input("\nRas Character (1-4) :")
                    if ras == "1":
                        ras = "human"
                        break
                    elif ras == "2":
                        ras = "dwarf"
                        break
                    elif ras == "3":
                        ras = "elf"
                        break
                    elif ras == "4":
                        ras = "orc"
                        break
                    else:
                        print("Pilihan invalid, pilihan hanya (1-4)")
                
                print("\nStatistik Character")

                while True:
                    try:
                        hp = int(input("HP: "))
                        break
                    except ValueError:
                        print("Input invalid, masukkan angka yang benar.")

                while True:
                    try:
                        mp = int(input("MP: "))
                        break
                    except ValueError:
                        print("Input invalid, masukkan angka yang benar.")

                while True:
                    try:
                        deff = int(input("Def: "))
                        break
                    except ValueError:
                        print("Input invalid, masukkan angka yang benar.")

                while True:
                    try:
                        str = int(input("Str: "))
                        break
                    except ValueError:
                        print("Input invalid, masukkan angka yang benar.")

                while True:
                    try:
                        agi = int(input("Agi: "))
                        break
                    except ValueError:
                        print("Input invalid, masukkan angka yang benar.")

                while True:
                    try:
                        intt = int(input("Int: "))
                        break
                    except ValueError:
                        print("Input invalid, masukkan angka yang benar.")      

                # Menambahkan karakter dan statistik ke dalam list
                print(f"\nCharacter {nama} Ditambahkan")
                character = [nama, role, ras]
                statistik = [hp, mp, deff, str, agi, intt]
                characters.append(character)
                statistiks.append(statistik)
                
            elif pilihan == "3":
                # Memperbarui statistik karakter
                name = input("Nama karakter yang akan diupdate : ").lower()   

                if not characters:
                    print("\nCharacter Tidak Ditemukan")
                for i in range(0,len(characters)):
                                       
                    if characters[i][0] == name:
                        print(f"\n======== Pilihan yang akan di ganti ========")
                        print(f"1. Nama             6. Def")
                        print(f"2. Role             7. Str")
                        print(f"3. Ras              8. Agi")
                        print(f"4. HP               9. Int")
                        print(f"5. MP")
                    
                        pilihan = input("\nStatistik yang ingin diupdate :")
                        if pilihan == '1':
                            value = input("Masukkan Nama Baru :").lower()

                            # Cek duplikasi nama baru
                            while any(value == character[0] for character in characters):
                                print(f"Character Dengan Nama '{value}' Sudah ada, masukan nama baru.")
                                value = input("Nama Character :").lower()

                            characters[i][0] = value  # Update nama karakter
                            print(f"Nama karakter telah diperbarui menjadi '{value}'.")
                            break
                                                    
                        elif pilihan == '2':
                            while True:
                                print("\n===== Role Character =====")  
                                print("1. Warrior        3. Priest")
                                print("2. Wizard         4. Paladin")     
                                role = input("\nRole Character (1-4) :")
                                if role == "1":
                                    role = "warrior"
                                    print("\nRole Warrior ditambahkan")
                                    break
                                elif role == "2":
                                    role = "wizard"
                                    print("\nRole Wizard ditambahkan")
                                    break
                                elif role == "3":
                                    role = "priest"
                                    print("\nRole priest ditambahkan")
                                    break
                                elif role == "4":
                                    role = "paladin1"
                                    print("\nRole paladin ditambahkan")
                                    break
                                else:
                                    print("\nPilihan invalid, pilihan hanya (1-4)")
                            characters[i][1] = role  
                            break
                        elif pilihan == '3':
                            while True:            
                                print("\n===== Ras Character =====")
                                print("1. Human         3. Elf")
                                print("2. Dwarf         4.Orc")        
                                ras = input("\nRas Character (1-4) :")
                                if ras == "1":
                                    ras = "human"
                                    print("\nRas human ditambahkan")
                                    break
                                elif ras == "2":
                                    ras = "dwarf"
                                    print("\nRas dwarf ditambahkan")
                                    break
                                elif ras == "3":
                                    ras = "elf"
                                    print("\nRas elf ditambahkan")
                                    break
                                elif ras == "4":
                                    ras = "orc"
                                    print("\nRas orc ditambahkan")
                                    break
                                else:
                                    print("\nPilihan invalid, pilihan hanya (1-4)")
                            characters[i][2] = ras                 
                            break
                        elif pilihan == '4':
                            while True:
                                try:
                                    value = int(input("Masukkan nilai baru untuk HP: "))
                                    statistiks[i][0] = value
                                    break
                                except ValueError:
                                    print("Input tidak valid, masukkan angka yang benar.")
                            break
                        elif pilihan == '5':
                            while True:
                                try:
                                    value = int(input("Masukkan nilai baru untuk MP: "))
                                    statistiks[i][1] = value
                                    break
                                except ValueError:
                                    print("Input tidak valid, masukkan angka yang benar.")
                            break
                        elif pilihan == '6':
                            while True:
                                try:
                                    value = int(input("Masukkan nilai baru untuk Def: "))
                                    statistiks[i][2] = value
                                    break
                                except ValueError:
                                    print("Input tidak valid, masukkan angka yang benar.")
                            break
                        elif pilihan == '7':
                            while True:
                                try:
                                    value = int(input("Masukkan nilai baru untuk Str: "))
                                    statistiks[i][3] = value
                                    break
                                except ValueError:
                                    print("Input tidak valid, masukkan angka yang benar.")
                            break
                        elif pilihan == '8':
                            while True:
                                try:
                                    value = int(input("Masukkan nilai baru untuk Agi: "))
                                    statistiks[i][4] = value
                                    break
                                except ValueError:
                                    print("Input tidak valid, masukkan angka yang benar.")
                            break
                        elif pilihan == '9':
                            while True:
                                try:
                                    value = int(input("Masukkan nilai baru untuk Int: "))
                                    statistiks[i][5] = value
                                    break
                                except ValueError:
                                    print("Input tidak valid, masukkan angka yang benar.")
                            break
                        else:
                            print("\nStatistik invalid.")
                            break
                    elif i == len(characters)-1:
                        print("\nCharacter Tidak Ditemukan")  
           
            elif pilihan == "4":
                print("\nMenghapus Character")
                name = input("Character yang akan dihapus :").lower()
                if not characters :
                    print("\nTidak Ada Character")
                for i in range(0,len(characters)):
                    if characters[i][0] == name:               
                        print(f"\nCharacter {characters[i][0]} Telah Dihapus")
                        del characters[i]
                        del statistiks[i]
                        break
                    elif i == len(characters)-1:
                        print(f"\nTidak Ada Character Bernama {name}")
            
            elif pilihan == "5":
                break
            
            else:
                print("\nPilihan hanya (1-5)")
        
        else:
            print("\n==== Manajemen Statistik Character ====")
            print("1. Tampilkan Character")
            print("2. Keluar")
            pilihan = input("Pilih :")

            if pilihan == "1":
                if not characters:
                    print("\nCharacter Belum Ada")
                else :
                    for i in range(0,len(characters)):
                        print(f"\n======== Character {i + 1} ========")
                        print(f"Nama : {characters[i][0]}")
                        print(f"Role : {characters[i][1]}")
                        print(f"Ras : {characters[i][2]}")
                        print(f"\nStatistik :")
                        print(f"Hp : {statistiks[i][0]}")
                        print(f"MP : {statistiks[i][1]}")
                        print(f"Def : {statistiks[i][2]}")
                        print(f"Str : {statistiks[i][3]}")
                        print(f"Agi : {statistiks[i][4]}")
                        print(f"Int : {statistiks[i][5]}")
                        print(f"===============================")        
            
            if pilihan == "2": 
                break   
print("Terima Kasih Karena Sudah Mencoba Program ini")  