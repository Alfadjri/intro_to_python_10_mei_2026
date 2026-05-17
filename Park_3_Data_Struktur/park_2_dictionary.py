
# CRUD
# Create
list_siswa = {
    "Kelas" : 12,
    "Jurusan" : ["Ipa","Ips"],
    "Nama_Ketua" : "Udin"
}
# read
print(f"Data Mentah : {list_siswa}")
print(f"Siapa nama ketua kelas : {list_siswa["Nama_Ketua"]}")
print(f"Kelas ini harus jurusan IPS : {list_siswa["Jurusan"][1]}")
# Update
list_siswa["Nama_Ketua"] = "ICA"
list_siswa["Total"] = 40
print(f"Data Update : {list_siswa}")
# Delete
del list_siswa["Total"]
print(f"Data Delete : {list_siswa}")