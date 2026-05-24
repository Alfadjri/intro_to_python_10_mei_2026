#kasus
#mengamati hewan

class Hewan:
    nama_hewan = "default"
    jenis_hewan = "default"
    _asdwasdwasdwaa= 10 

    # constructor
    def __init__(self,nama,jenis):
        self.nama_hewan = nama
        self.jenis_hewan = jenis

    def makan(self):
        print("Hewan sedang makan")
    # Set and get
    def get_usia(self):
        return self._asdwasdwasdwaa
    
    def set_usia(self,umur):
        self._asdwasdwasdwaa = umur



kucing = Hewan("Tom","Anggora")
print(f"Nama\t: {kucing.nama_hewan}")
print(f"Jenis\t: {kucing.jenis_hewan}")
print(f"Usia\t: {kucing.get_usia()}")
print("Kegiatan Hewan : ")
kucing.makan()
print("Update value")
kucing.set_usia(20)
print(f"Usia\t: {kucing.get_usia()}")