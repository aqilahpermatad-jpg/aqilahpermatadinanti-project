#TRANSFER STATEMENTS 

#1. Break Statements
for i in range(20):
    if i == 6:
        break
    print(i)

#2 Continue Statement 
for i in range(8): 
    if i == 2:
        continue
    print(i)

#3 Pass Statement    
nilai = 90
if nilai > 80:
    pass
else:
    print("Nilai belum lulus")

#4 Return Statement
def add(a, b):
    return a + b

hasil = add(6, 7)
print(hasil)  

hasil = 0

def hitung(a, b):
    global hasil
    hasil = a + b

hitung(8, 9)
print(hasil)