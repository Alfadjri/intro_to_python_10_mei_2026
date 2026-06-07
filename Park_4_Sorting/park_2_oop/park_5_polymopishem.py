from abc import ABC, abstractmethod

class Hewan(ABC):
    nama_hewan = "default"
    jenis_hewan = "default"
    _umur_hewan = 10 

    # constructor
    def __init__(self,nama,jenis):
        self.nama_hewan = nama
        self.jenis_hewan = jenis

    def makan(self):
        print("Hewan sedang makan")
    
    @abstractmethod
    def suara(self):
        pass

    def set_usia(self,umur):
        self._umur_hewan = umur
    def get_usia(self):
        return self._umur_hewan

    def profile(self):
        print(f"Nama\t: {self.nama_hewan}")
        print(f"Jenis\t: {self.jenis_hewan}")
        print(f"Usia\t: {self.get_usia()}")

class Kucing(Hewan):
    def __init__(self,nama,jenis):
         super().__init__(nama, jenis)
     
    def suara(self):
        print("Meow!!!!!")

class Dog(Hewan):
    def __init__(self,nama,jenis):
        super().__init__(nama, jenis)
    
    def suara(self):
        print("Woffff!!!!")


def profile(Hewan):
    Hewan.profile()


tom = Kucing("Tom","Anggora")
spike = Dog("Spike","Bulldog")

spike.profile()

profile(spike)

