# LIST
# -> struktur data di python yang digunakan untuk menyimpan koleksi elemen dalam variabel tertentu
# -> bisa berupa tipe data apapun & bisa memiliki tipe data berbeda
# -> Jika tipe datanya campur --> akan menjadi tipe data ANY

# Karakteristik:
# - bisa diubah / mutable
# - boleh tidak terurut / unordered
# - boleh ada perulangan / allow duplicate item

#-----------------------------------------------------------------------------------------

my_list = [1, "dua", True, 4.5]
print(my_list)

# ACCESS element with INDEX

print(my_list[1])       # Print
my_list[2] = 88.88      # Change
print(my_list[2])

#-----------------------------------------------------------------------------------------

# APPEND 

# -> menambahkan Element ke List di paling BELAKANG
my_list.append("oke")
print(my_list)

#-----------------------------------------------------------------------------------------

# INSERT

# -> menambahkan Element di POSISI tertentu
my_list.insert(2, "Rabu")
print(my_list)

# SEARCH -> in & not in
if "oke" in my_list:
    print("Ada oke di my list")
else : print("tidak ada oke di my list")

for i in range(len(my_list)):
    if my_list[i] == "dua":
        print(my_list[i])

# Mencari kata dengan awalan tertentu
# method startwith --> harus tipe datanya spesifik

for i in range(len(my_list)):
    if str(my_list[i]).startswith("o"): # typecasting semua elemen ke string
        print(my_list[i])

#-----------------------------------------------------------------------------------------

# DELETE -> del --> berdasarkan indeks
arr = [0, 1, 2, 3, 4]

del arr[2]  # indeks spesifik
print(arr)

del arr     # keseluruhan
# print(arr)    --> menyebabkan Error karena "arr" sudah dihapus


# POP --> berdasarkan indeks
arr = [0, 1, 2, 3, 4]

arr.pop(4)
print(arr)


# REMOVE --> berdasarkan item
arr = [0, 1, 2, 3, 4]

arr.remove(3)
print(arr)

#-----------------------------------------------------------------------------------------

# SORT --> method

# mengurutkan element di list dengan MENGUBAH LIST ASLI
# Tipe data HARUS SAMA (kecuali int & float)

# Array of Numbers
num = [5, 3, 4, 2]
num.sort()              # ascending
print(num)

num.sort(reverse=True)  # descending
print(num)

# Array of String
arr_str = ["Beta", "Charlie", "Delta", "Alpha", "Echo"]
arr_str.sort()
print(arr_str)

# Array of Bool
arr_bool = [True, False, True]
arr_bool.sort()
print(arr_bool) # --> output alpabetik, False duluan

# Array dengan TIPE DATA BERBEDA
# --> di typecasting ke string umumnya

arr_rand = [1, 2.4, "tiga", "empat", True]

arr_rand.sort(key=str) #diubah ke tipe data String semua --> default int & float duluan > boolean > string
print(arr_rand)


#SORTED --> function
# mengurutkan element di list dengan MEMBUAT LIST BARU
# bisa untuk tuple, set, string, dll
# tipe data HARUS SAMA
arr = ["Beta", "Charlie", "Delta", "Alpha", "Echo"]

arr_sorted = sorted(arr)
print(arr_sorted)

#-----------------------------------------------------------------------------------------

# SLICING

# -> Mengakses Elemen dalam range spesifik
# syntax --> nama_list[start:end:step]  
#       --> start, end dan step opsional --> step harus positif
# tipe data boleh CAMPUR / ANY

arr = [0, 1, True, 3, 4.8, "lima", 6]

print(arr[:])   # print semua element
print(arr[::])

print(arr[3:]) # start di idx ke-3 hingga indeks terakhir

print(arr[:5]) # start dari awal hingga SEBELUM idx ke-5

print(arr[1:5:2]) #start dari idx ke-1 hingga sebelum idx ke-5 dengan step + 2
                    # idx ke-5 tidak muncul karena SEBELUM idx ke-5

print(arr[::2]) # step = 2 --> ambil array dari awal sampai akhir dengan step 2


# NEGATIVE INDEXING
# -> berguna untuk mengakses elemen dari akhir list

print(arr[-2:]) # mulai dari indeks ke-2 dari BELAKANG

print(arr[-7:-2])   # mulai dari indeks ke-7 dari BELAKANG hingga SEBELUM ke-2 dari BELAKANG

print(arr[-7:-1:2]) # STEP-nya 2 kali / langkahin 1

rev_arr = arr[::-1] # REVERSE ARRAY dengan negative indexing
print(rev_arr)
