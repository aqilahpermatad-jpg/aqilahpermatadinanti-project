
#contoh penerapan library python
import requests

response = requests.get("https://api.github.com")
print(response.status_code)
print(response.text)

#library math 
import math

print(math.sqrt(20))
print(math.pi)

#library random

import random
angka = random.randint(1, 20)
print("Angka acak:", angka)

#pip freeze > requirements.txt (djalankan di terminal untuk menyimpan library yang digunakan dalam proyek)

#library datetime

from datetime import datetime
sekarang = datetime.now()
print("Tanggal dan waktu sekarang:", sekarang)

#studi kasus sederhana 

import random 

nilai = random.randint(60, 100)
print ("nilai:", nilai)

if nilai >= 80:
    print("Lulus")
else:
    print("Tidak Lulus")

#CONDITIONAL STATEMENT

nilai = 90 
if nilai >= 80: 
    print("Nilai: A")
elif nilai >= 70:
    print("Nilai: B+")
else :
    print("Nilai: C")

password = input('Enter password ')
if password == "aqilahpermatadinanti1":
    print("Correct password")
else:
    print("Incorrect Password")

#2
def user_check(choice):
    if choice == 2:
        print("student 2")
    elif choice == 3:
        print("student 3") 
    elif choice == 4:
        print("student 4")   
    else: 
        print("Wrong Entry")
user_check(2)
user_check(3)
user_check(4)
user_check(5)
 
 ##KARENA CODING SUDAH TIDAK BISA RUNNING DENGAN BAIK, JADI DI PINDAHKAN KE AQILAH PROGRAM 2##

# Kode baru: Fungsi sederhana
def hello_world():
    print("Hello, World! Ini kode baru di Aqilah Program.py")

hello_world()


