#3 menggunakan input dari pengguna


x =int(input("Masukkan Nilai x: "))  
if x > 7:
    print("x lebih besar dari 7")
elif x == 5:
    print("x sama dengan 7")
else:
    print("x lebih kecil dari 7")

#menggunakan if bersarang 

x = int(input("masukkkan nilai x: "))
if x > 0: 
    print("x juga bilangan positif")
    if x % 2 == 0:
        print("x juga bilangan genap")
    else: 
        print("x adalah bilangan ganjil")
elif x == 0:
    print("x adalah nol")   
else:
    print("x adalah bilangan negatif")  

#menggunakan operator logika dalam if 

x = int(input("masukkkan nilai x: "))    
if x > 0 and x % 2 == 0: 
    print("x adalah bilangan positif dan genap")
elif x > 0 and x %2 !=0:
    print("x adalah bilangan positif dan ganjil")
else:
    print("x bukan bilangan positif")    

#menggunakan ternary operator (if dalam satu baris)

x = int(input("masukkkan nilai x: "))
status = "positif" if x > 0 else "negatif atau nol"
print(f"x adalah bilangan {status}")

#TRANSFER STATEMENTS MEMPUNYAI FOLDER SENDIRI, TIDAK BISA RUNNING JIKA BERADA DENGAN KODE LAIN##

# Menggunakan for (jumlah sudah pasti 6 kali)
for i in range(6):
    print("Perulangan ke-", i)

# Menggunakan while
i = 0
while i < 6:
    print("Perulangan ke-", i)
    i += 1

#KONTROL DALAM PENGULANGAN 

#1. Break   
for i in range(20):
    if i == 5:
        break
    print(i)

#Continue
for i in range(10):
    if i == 3:
        continue
    print(i)    

#Else
for i in range(7):
    print(i)
else:
    print("Loop selesai tanpa break")   

#NESTED LOOP(PERULANGAN BERSARANG) 
for i in range(6):
    for j in range(i+1):
        print("*", end="")
    print()

#Aplikasi lterasi dalam Algoritma

#1. Menghitung Jumlah Total 
angka = [20, 30, 40, 50]
total = 0
for nilai in angka:
    total += nilai

print("Total:", total)  

#2. Menghitung Faktorial 
n = 7
faktorial = 1

for i in range(1, n+1):
    faktorial *= i

print("Faktorial:", faktorial)

#3. Validasi Input Dengan While
nilai = -1
while nilai < 0:
    nilai = int(input("Masukkan angka positif: "))

print("Input diterima")