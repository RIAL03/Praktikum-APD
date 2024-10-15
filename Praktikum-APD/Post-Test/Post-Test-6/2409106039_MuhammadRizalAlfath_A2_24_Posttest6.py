# Untuk Login Menjadi Admin
# Username = rizal
# Password = 039

admin = {"rizal": "039"}
user = {}

characters = {}
statistiks = {}

program = True
while program:
    ulang1 = True
    while ulang1:
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
                    if login_admin in admin and admin[login_admin] == password_admin:
                        print("\nAnda Berhasil Login Sebagai admin")
                        akses = True
                        ulang1 = False
                        break
                elif login == "2":
                    if login_admin in user and user[login_admin] == password_admin:
                        print("\nLogin Berhasil Sebagai User")
                        akses = False
                        ulang1 = False
                        break

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
            while login_user in user:
                print(f"Username '{login_user}' sudah ada, masukkan Username Baru.")
                login_user = input("Username Baru: ").lower()

            user[login_user] = password_user
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
                else:
                    for name, char in characters.items():
                        index = list(characters.keys()).index(name)
                        print(f"\n======== Character {index + 1} ========")
                        print(f"Nama : {char['name']}")
                        print(f"Role : {char['role']}")
                        print(f"Ras : {char['ras']}")
                        print(f"\nStatistik :")
                        if name in statistiks:
                            print(f"Hp : {statistiks[name]['hp']}")
                            print(f"MP : {statistiks[name]['mp']}")
                            print(f"Def : {statistiks[name]['def']}")
                            print(f"Str : {statistiks[name]['str']}")
                            print(f"Agi : {statistiks[name]['agi']}")
                            print(f"Int : {statistiks[name]['int']}")
                        else:
                            print("Statistik tidak ditemukan.")
                        print(f"===============================")

            elif pilihan == "2":
                print("\nMembuat Character baru")
                nama = input("Nama Character :").lower()

                # Cek duplikasi nama sebelum melanjutkan
                while nama in characters:
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

                # Menambahkan karakter dan statistik ke dalam dictionary
                print(f"\nCharacter {nama} Ditambahkan")
                characters[nama] = {
                    "name": nama, 
                    "role": role, 
                    "ras": ras
                    }
                
                statistiks[nama] = {
                    "hp": hp, 
                     "mp": mp, 
                    "def": deff, 
                    "str": str, 
                    "agi": agi, 
                    "int": intt
                    }

            elif pilihan == "3":
                # Memperbarui statistik karakter
                name = input("Nama karakter yang akan diupdate : ").lower()

                if name not in characters:
                    print("\nCharacter Tidak Ditemukan")
                else:
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
                        while value in characters:
                            print(f"Character Dengan Nama '{value}' Sudah ada, masukan nama baru.")
                            value = input("Nama Character :").lower()

                        characters[value] = characters.pop(name)  # Update nama karakter
                        characters[value]["name"] = value
                        print(f"Nama karakter telah diperbarui menjadi '{value}'.")

                    elif pilihan == '2':
                        while True:
                            print("\n===== Role Character =====")  
                            print("1. Warrior        3. Priest")
                            print("2. Wizard         4. Paladin")     
                            role = input("\nRole Character (1-4) :")
                            if role == "1":
                                characters[name]['role'] = "warrior"
                                print("\nRole Warrior ditambahkan")
                                break
                            elif role == "2":
                                characters[name]['role'] = "wizard"
                                print("\nRole Wizard ditambahkan")
                                break
                            elif role == "3":
                                characters[name]['role'] = "priest"
                                print("\nRole priest ditambahkan")
                                break
                            elif role == "4":
                                characters[name]['role'] = "paladin"
                                print("\nRole paladin ditambahkan")
                                break
                            else:
                                print("\nPilihan invalid, pilihan hanya (1-4)")

                    elif pilihan == '3':
                        while True:
                            print("\n===== Ras Character =====")
                            print("1. Human         3. Elf")
                            print("2. Dwarf         4. Orc")        
                            ras = input("\nRas Character (1-4) :")
                            if ras == "1":
                                characters[name]['ras'] = "human"
                                print("\nRas human ditambahkan")
                                break
                            elif ras == "2":
                                characters[name]['ras'] = "dwarf"
                                print("\nRas dwarf ditambahkan")
                                break
                            elif ras == "3":
                                characters[name]['ras'] = "elf"
                                print("\nRas elf ditambahkan")
                                break
                            elif ras == "4":
                                characters[name]['ras'] = "orc"
                                print("\nRas orc ditambahkan")
                                break
                            else:
                                print("\nPilihan invalid, pilihan hanya (1-4)")

                    elif pilihan == '4':
                        while True:
                            try:
                                hp = int(input("HP: "))
                                statistiks[name]['hp'] = hp
                                break
                            except ValueError:
                                print("Input invalid, masukkan angka yang benar.")

                    elif pilihan == '5':
                        while True:
                            try:
                                mp = int(input("MP: "))
                                statistiks[name]['mp'] = mp
                                break
                            except ValueError:
                                print("Input invalid, masukkan angka yang benar.")

                    elif pilihan == '6':
                        while True:
                            try:
                                deff = int(input("Def: "))
                                statistiks[name]['def'] = deff
                                break
                            except ValueError:
                                print("Input invalid, masukkan angka yang benar.")

                    elif pilihan == '7':
                        while True:
                            try:
                                str = int(input("Str: "))
                                statistiks[name]['str'] = str
                                break
                            except ValueError:
                                print("Input invalid, masukkan angka yang benar.")

                    elif pilihan == '8':
                        while True:
                            try:
                                agi = int(input("Agi: "))
                                statistiks[name]['agi'] = agi
                                break
                            except ValueError:
                                print("Input invalid, masukkan angka yang benar.")

                    elif pilihan == '9':
                        while True:
                            try:
                                intt = int(input("Int: "))
                                statistiks[name]['int'] = intt
                                break
                            except ValueError:
                                print("Input invalid, masukkan angka yang benar.")

                    print(f"\nCharacter {name} berhasil diupdate.")

            elif pilihan == "4":
                # Menghapus karakter
                name = input("Nama karakter yang akan dihapus :").lower()
                if name not in characters:
                    print("Character tidak ditemukan")
                else:
                    del characters[name]
                    del statistiks[name]
                    print(f"\nCharacter {name} berhasil dihapus")

            elif pilihan == "5":
                ulang1 = True
                print("Kembali Ke Menu Login")
                break

        elif akses == False:
            print("\n==== Menu User ====")
            print("1. Tampilkan Character")
            print("2. Keluar")
            pilihan_user = input("Pilih 1-2 :")
            if pilihan_user == "1":
                if not characters:
                    print("\nCharacter Belum Ada")
                else:
                    for name, char in characters.items():
                        index = list(characters.keys()).index(name)
                        print(f"\n======== Character {index + 1} ========")
                        print(f"Nama : {char['name']}")
                        print(f"Role : {char['role']}")
                        print(f"Ras : {char['ras']}")
                        print(f"\nStatistik :")
                        if name in statistiks:
                            print(f"Hp : {statistiks[name]['hp']}")
                            print(f"MP : {statistiks[name]['mp']}")
                            print(f"Def : {statistiks[name]['def']}")
                            print(f"Str : {statistiks[name]['str']}")
                            print(f"Agi : {statistiks[name]['agi']}")
                            print(f"Int : {statistiks[name]['int']}")
                        else:
                            print("Statistik tidak ditemukan.")
                        print(f"===============================")

            elif pilihan_user == "2":
                ulang1 = True
                print("Kembali Ke Menu Login")
                break
print("Terima Kasih sudah mencoba program ini")