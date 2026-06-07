#kasus
#mengamati hewan

class Hewan:
    nama_hewan = "default"
    jenis_hewan = "default"
    _usia_hewan= 10 

    # constructor
    def __init__(self,nama,jenis):
        self.nama_hewan = nama
        self.jenis_hewan = jenis

    def makan(self):
        print("Hewan sedang makan")
    # Set and get
    def get_usia(self):
        return self._usia_hewan
    
    def set_usia(self,umur):
        self._usia_hewan = umur
    
    def get_profile(self):
        return f"{self.nama_hewan} adalah {self.jenis_hewan} yang berusia {self._usia_hewan} tahun"



kucing = Hewan("Tom","Anggora")
print(kucing.get_profile())
print("Kegiatan Hewan : ")
kucing.makan()
print("Update value")
kucing.set_usia(20)
print(kucing.get_profile())