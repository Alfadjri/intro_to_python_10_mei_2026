# For
# tahu kapan mulai dan kapan berhenti sekaligus tahapan menuju berhenti
print("====for====")
for index in range(10):
    print(f"{index}.Maaf!!")
# foreach
# kita tau tipe data 
buahs = ["Semangka","Melon","Anggur","Jeruk","Mangga"]
print("List foreach")
for buah in buahs:
    print(f"{buah}")

# While
# tahu syarat berhenti bekerja 
jumlah_siswa = 5
while jumlah_siswa < 10:
    print("siswa tidak lengkap")
    jumlah_siswa += 1

# Continue and break

nomer = 1 
while nomer <= 100:
    if nomer % 2 == 0:
        nomer += 1
        continue #mau skip 1 putaran atau 1 loop
    
    print(f"{nomer}")
    nomer += 1
    if nomer == 20:
        break #memakasa untuk memberhentikan loop 
