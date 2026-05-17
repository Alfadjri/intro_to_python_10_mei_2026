# non Void
# function yang mengeluarkan hasil kalkulasi 
# ciri-ciri ada return

def penjumlahan(nilai1,nilai2):
    hasil = nilai1 + nilai2
    return hasil

# Void
# funciton yang tidak mengeluarkan kalkulasi nilai apapaun
# def nama_function(paramter/syarat):
#  sekenario yang akan kamu gunakan
def format_nama(nama_siswa):
    print(f"Nama : {nama_siswa}")
    print(f"==================")

siswas = ["Alfadjri","Dwi","Fadhilah","Dika","Galih"]
print(f"=====List=========")
format_nama(siswas[0])
format_nama(siswas[1])
format_nama(siswas[2])
format_nama(siswas[3])
format_nama(siswas[4])

print("================")
hasil = penjumlahan(10,2)
print(f"Hasil dari 10 + 2 : {hasil}")