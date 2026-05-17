# Numerik type
# integer
# integer bilangan bulat
x = 32767
print("Contoh tipe data Integer (int) : {0}".format(x))
# float
# float bilangan desimal
y = 9.8
print("Contoh tipe data float (float) : {0}".format(y))
# Complex
# Complex bilangan imajiner
z = 3 + 2j
print("Contoh tipe data Complex (Complex) : {0}".format(z))
# Squence type
# list
# list tipe data yang dapat menampung lebih dari 1 data
a = [1,2,3,4,5]
print("Contoh tipe data list (list) : {0}".format(a))
# truplet
# truplet tipe data yang dapat menampung lebih dari 1 data tapi tidak bisa di ubah
b = (6,7,8,9,0)
print("Contoh tipe data truplet (truplet) : {0}".format(b))
# range
# range tipe data yang dapat yang mengeluarkan nilai berurutan
c = range(1,5)
print("Contoh tipe data range (range) : {0}".format(c))

# String
# String tipe data text
nama = "Alfadjri Dwi Fadhilah"
print("Contoh tipe data String (Str) : {0}".format(nama))

# Dictionary
# Dictionary tipe data profile
profile = { "nama" : nama , "age" : 25}
print("Contoh tipe data Dictionary (dict) : {0}".format(profile["age"]))

# Boolean
# Boolean tipe data yang hanya memili dua nilai True (1) or False(0)
boleantype = True
print("Contoh tipe data Boolean (bool) : {0}".format(boleantype))

#set type
# Set
# Set tipe data yang tidak bisa di ubah
settype = {1,2,3,4,5}
print("Contoh tipe data Set (Set) : {0}".format(settype))
# frozenset
# frozenset tipe data yang tidak bisa di ubah
frozensettype = frozenset(a)
print("Contoh tipe data frozenset (frozenset) : {0}".format(frozensettype))

# binary
biner = 0b01000001
# tidak baik
# desimal = int(biner)
# char = chr(desimal) # conversi
char = chr(int(biner))
print("Contoh tipe data binary (binary) : {0}".format(char))


