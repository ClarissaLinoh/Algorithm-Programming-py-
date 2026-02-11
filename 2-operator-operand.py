#arithmetic operator
# -> operator matematis 

a = 4
b = 3

print(a+b) #plus
print(a-b) #minus
print(a*b) #kali
print(a/b) #bagi -> float
print(a//b) #floor -> bagi dibulatkan kebawah -> integer
print(a%b) #modulo -> sisa bagi
print(a**b) #pangkat -> a pangkat b

#ASSIGMENT OPERATOR
#operator yang memberikan value ke suatu variable
# hanya ada 1 yaitu sama dengan (=)

a = 4
b = 3
print(a , b)

#SHORTHAND OPERATOR
#arithmetic operator + assigment operator 
a += b  #a = a + b
print(a) #nilai a menjadi 7
a -= b  #a = a - b --> a = 7 - 3
print(a) #nilai a menjadi 4
a *= b  #a = a * b
print(a) #12
a /= b  #a = a / b
print(a) #4.0 --> float
#a = 4.0
#b = 3
#operasi antara integer & float akan menghasilkan float
a //= b  #a = a // b
print(a) #1.0
a %= b  #a = a % b
print(a) #1.0
a **= b  #a = a ** b
print(a) #1.0

#RELATIONAL OPERATOR -> menghasilkan nilai boolean (true / false)
#operator yang membandingkan 2 value
a = 8
b = 8
c = a == b #apakah a sama dengan b
print(c)
c = a != b #apakah a tidak sama dengan b
print(c)
c = a > b #apakah a lebih besar dari b
print(c)
c = a < b #apakah a lebih kecil dari b
print(c)
c = a >= b #apakah a lebih besar sama dengan b
print(c)
c = a <= b #apakah a lebih kecil sama dengan b
print(c)


#LOGICAL OPERATOR
#berfungsi untuk melakukan operasi logis
#nilai hasil boolean (true/false)
a = 4
b = 9
c = a < b and a != b 
#apakah a lebih kecil dari b DAN (and) apakah a tidak sama dengan b
#AND semua kondisi harus benar
print(c)

c = a < b or a == b 
#apakah a lebih kecil dari b ATAU (or) a sama dengan b
#untuk OR salah satu kondisi benar masih boleh
print(c)

c = not (a < b and a != b)
print(c)
#NOT membalikkan nilai -> True jadi false, false jadi true


#BITWISE OPERATOR
#operator yang bekerja pada level bit / biner

a = 23
b = 37
print(a & b) #AND --> keduanya harus 1
print(a | b) #OR --> salah satu atau keduanya 1
print(a ^ b) #exclusive OR (XOR) --> hanya salah satu bernilai 1
print(~a) #membalikkan nilainya
    #ditampilkan bentuk komplement nya
    #(bilangan tsb + 1) * (-1)

#syntax nya 
# angkaYgDiubah << / >> berapa kali di shift
print(23<<2) #left shift
print(23>>2) #right shift


#ASSOCIATIVE & PRECENDENCE
a = 2
b = 3
c = 5

d = a**a + (-b) * c + (a * b) / 2
# parentheses () dikerjakan pertama
# a**a + (-b) * c + 6 / 2

#Eksponen/pangkat **
# 4 + (-b) * c + 6 / 2

#Perkalian * --> karena yang paling dekat ke kiri
# 4 + (-15) + 6 /2

# Pembagian (/)
# 4 + (-15) + 3

#Penambahan 1
# - 11 + 3

#penambahan 2
# -8

print(d)


