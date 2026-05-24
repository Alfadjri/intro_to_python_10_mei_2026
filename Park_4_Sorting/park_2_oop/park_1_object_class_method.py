#kasus
#mengamati hewan

class Hewan:
    nama_hewan = "default"
    jenis_hewan = "default"
    _umur_hewan = 10 

    # constructor
    def __init__(self,nama,jenis):
        self.nama_hewan = nama
        self.jenis_hewan = jenis

    def makan(self):
        print("Hewan sedang makan")

# Cara memanggil
kucing = Hewan("Tom","Anggora")

print(f"Nama\t: {kucing.nama_hewan}")
print(f"Jenis\t: {kucing.jenis_hewan}")
# print(f"Usia\t: {kucing.umur}")
print("Kegiatan Hewan : ")
kucing.makan()