# LIST OF WORD
# Latihan Pra-Kuis AlgoProg DBI 2026


#Variabel untuk menampung pilihan user
choice = 8  #diisi dengan nilai random yang tidak sama dengan kondisi False While loop (dalam kasusu '6')

#List kosong
list = []

# Repetition While loop
# --> Selama input bukan '6' maka ulangi terus semua blok kode yang ada dalam while loop
while choice != '6' :

    print("\n" * 5)     #[opsional] hanya untuk merapikan tampilan

    # MENU UTAMA
    print("-- LIST OF WORDS --")
    print("1. Add word")
    print("2. Sort word")
    print("3. Find word")
    print("4. Show list")
    print("5. Delete word")
    print("6. Quit")

    # Input user --> secara otomatis input bertipe data string --> disimpan ke variabel 'choice'
    # sehingga digunakan '1' bukan 1  --> jika ingin menggunakan 1 maka lakukan typecasting ke integer
    choice = input(">> ")

    # Selection - Match case
    # untuk mengarahkan user ke menu yang dipilihnya
    match choice:

        # MENU 1. Add Word
        case '1':
            print("---- Option 1 : Add Word ----")

            # index berdasarkan input user --> di typecasting ke integer karena index harus berupa angka
            index = int (input("Input position [number]: "))
            # input kata yang ingin dimasukkan
            data = input("Input your word [text] : ")
            # digunakan method insert untuk memasukkan data kedalam list berdasarkan index yang dipilih
            list.insert(index, data)

        # MENU 2. Sort Word
        case '2':
            print("---- Option 2 : Sort Word ----")

            # Input user untuk Ascending atau Descending --> disimpan ke variabel 'option'
            option = input("Ascending or descending  [A / D] ? ")

            # Selection untuk menentukan di sortir secara Ascending / Descending
            if option == 'A':
                list.sort()             #Jika input 'A' maka di sortir secara Ascending
            elif option == 'D':
                list.sort(reverse=True) # Jika input 'D' maka di sortir secara Descending
            else:
                print("Input should be A / D")  # Jika input bukan 'A' atau 'D' maka tidak dilakukan perubahan ke list
                continue                        # Continue sehingga bagian print sorted list tidak dijalankan dan kembali ke menu utama

            print(f"Sorted List = {list}")      # Menampilkan hasil list yang SUDAH TERSORT

            input()     #[Opsional] Hanya agar menunggu enter sebelum kembali ke menu utama

        # MENU 3. Find Word
        case '3':
            print("---- Option 3 : Find Word ----")
            # Input kata yang ingin dicari --> disimpan ke variabel 'search'
            search = input("What do you want to found? ")

            # Selection dan "in" digunakan untuk menemukan kata dalam list
            if search in list:  # Jika 'search' ada di dalam list maka lakukan:
                print(f"{search} exist!")
            else:               # Jika tidak maka lakukan:
                print(f"{search} is not exist!")  

            input()     #[Opsional] Hanya agar menunggu enter sebelum kembali ke menu utama

        # MENU 4. Show List
        case '4':
            print("---- Option 4 : Show List ----")
            print(list) # print list

            input()     #[Opsional] Hanya agar menunggu enter sebelum kembali ke menu utama

        # MENU 5. Delete Word
        case '5':
            print("---- Option 5 : Delete Word ----")

            # user meng-input kata yang ingin dihapus dan disimpan di variabel search
            # --> [!!] python case sensitive --> 'minggu' tidak sama dengan 'Minggu'
            search = input("What item do you want to delete ? ")

            # Selection untuk cek apakan kata yang ini dihapus ada atau tidak
            if search not in list:              # Jika kata tidak ada maka beritahu user tidak ada yang bisa dihapus
                print(f"{search} is not exist")
            else :                              # Jika kata ada:
                for i in range(len(list)):      # For loop mengecek setiap item list untuk mencari posisi kata
                    if(search == list[i]):      # Jika list ke-i sama dengan kata yang dicari (search)
                        del list[i]             # hapus list ke-i
                        break                   # break untuk menghentikan for loop --> TANPA break bisa ERROR 
                
                print(list) # Print list baru

        # MENU 6. QUIT
        case '6':
            print("Goodbye!")
    
        # DEFAULT --> jika input tidak diantara '1' - '6'
        case _ :
            print("Invalid Choice!")
            input()         #[Opsional] Hanya agar menunggu enter sebelum kembali ke menu utama

    
    
    