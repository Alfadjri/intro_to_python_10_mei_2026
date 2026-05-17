
# CRUD
# Create
# inisialisasi
buahs = ["Semangka","Melon","Pisang"]
# Read
print(f"List Buah-buahan {buahs}")
# Read Spesifik
print(f"Value in index 1 : {buahs[1]}")
print(f"value in index -1 : {buahs[-1]}")
# Update (sulit)
buahs[2] = "Anggur"
print(f"List Buah-buahan setelah di ubah {buahs}")
# Delete (sulit)
del buahs[2]
print(f"List Buah-buahan setelah di delete {buahs}")
buahs.append("Pisang")
buahs.append("Anggur")
print(f"List Buah-buahan setelah di add {buahs}")