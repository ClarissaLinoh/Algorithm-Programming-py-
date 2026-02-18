#SELECTION & REPETITION

#SELECTION
#--> program mengambil keputusan berdasarkan kondisi logis

a = 2
b = 8

#IF ELIF ELSE
if a > b:
    print(f"Nilai a = {a} lebih besar dari b = {b}")    #if hanya 1 & wajib ada
elif a < b:
    print(f"Nilai a = {a} lebih kecil dari b = {b}")    #elif boleh banyak & opsional
else :
    print(f"Nilai a = {a} lebih sama dengan b = {b}")   #else hanya 1 & opsional

#MATCH CASE
c = 8
match c:
    case 1:
        print("c value is 1")
    case 4:
        print("c value is 4")
    case 8:
        print("c value is 8")
    case _:
        print("c value is not 1, 4, or 8")

#SHORTHAND IF 
# --> statement hanya 1 sehingga bisa ditaruh di 1 line
if a*2 > b : print("a dikali 2 lebih besar dari b")
else : print("a dikali 2 lebih kecil dari b")

#PASS STATEMENT
# --> if tidak boleh kosong namun perlu digunakan, maka dipakai pass
if a - b == 0:
    pass    #dalam kasus ini jika a dikurang b bernilai 0 maka tidak akan ada output apapun
elif a - b > 0:
    print("a - b positif")  
else:
   print("a - b negatif")


#REPETITION
#--> Pengulangan yang dilakukan berdasarkan kondisi tertentu

# FOR
# --> mengulangi blok kode dengan JUMLAH PENGULANGAN DIKETAHUI

# For dalam string
for i in "apple":
    print(i, end=" ")

print("\n")

# For dalam array (list, tuple, set)
arr = [1, 4, 2, 3, 1, 2]
for i in arr:
    print(arr[i], end=" ")

print("\n")

# dengan RANGE
# satu parameter
for i in range(8):      # start dari indeks ke 0 sampai 7 --> iterasi sebanyak 8 kali
    print("*", end=" ")

print("\n")

#dua parameter
for i in range(2, 8):   # start dari indeks ke 2 sampai 7 --> iterasi 8 - 2 = 6 kali
    print("#", end=" ")

print("\n")

#tiga parameter
for i in range(2, 18, 2):  # start dari indeks ke 2 sampai 18 dan ditambah 2 per iterasi (18 - 2) / 2 = 16 / 2 = 8 kali
    print("$", end=" ")



#WHILE
#--> pengulangan yang dilakukan selama kondisi tetap TRUE

i = 0                   # inisiasi nilai variable
while i < 6:
    print(i, end=" ")
    i += 1              # WAJIB ada statemen yang MENGUBAH value variable sehingga MENCAPAI KONDISI --> increment / decrement

print("\n")


# JUMP OPERATOR --> break & continue

#Break 
# -->Jika kondisi terpenuhi iterasi dihentikan

for i in range(2, 100):
    if(i == 4): break   #ketika mencapai i = 4 iterasi dihentikan --> output hanya 2 dan 3
    print(i, end=" ")

print("\n")

x = 10
while x > 0:
    if(x == 6): break   #ketika mencapai x = 6 iterasi dihentikan --> output hanya 10, 9, 8, 7
    print(x, end=" ")
    x-=1

print("\n")


#Continue
#  --> Jika kondisi terpenuhi, SKIP iterasi

for i in range(2, 10):
    if(i == 4):
        i+=1        # HARUS ada PERUBAHAN NILAI --> jika tidak akan stuck di continue terus --> nilai i tetap 4 / infinite loop
        continue    #ketika mencapai i = 4 iterasi diskip --> angka 4 tidak ditampilkan
    print(i, end=" ")

print("\n")

x = 10
while x > 0:
    if(x == 6): 
        x -= 1      # HARUS ada PERUBAHAN NILAI --> jika tidak akan stuck di continue terus --> nilai i tetap 4 / infinite loop
        continue    #ketika mencapai x = 6 iterasi diskip --> angkat 6 tidak ditampilkan
    print(x, end=" ")
    x -= 1

print("\n")
