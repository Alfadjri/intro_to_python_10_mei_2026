import datetime

tanggal = datetime.datetime.now()
nama_atasan = "Ibu Gea Saskia"
Jabatan = "Manager SDM PT Ruang Keahilan"
Kota = "Bekasi"

# posisional formating
print("\t\t{0}\nYth.{1}\n{2}\n{3}".format(nama_atasan,tanggal,Jabatan,Kota))
# keyword formating
print("\t\t{tanggal}\nYth.{nama_atasan}\n{jabatan}\n{kota}".format(nama_atasan=nama_atasan,tanggal=tanggal,jabatan=Jabatan,kota=Kota))
# Singkat
print(f"\t\t{tanggal}\nYth.{nama_atasan}\n{Jabatan}\n{Kota}")