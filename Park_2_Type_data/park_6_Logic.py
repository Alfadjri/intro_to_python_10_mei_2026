# Case 
# Penilayan (KKM)
nilai = 80
print("======if======")
# if 
# if kondisi :
#  sekenario yang akan di lakukan 
if nilai > 80:
    print("Selamat kamu lulus dari ujian")
print("=====if-else=====")
# if 
# if kondisi :
#  sekenario yang akan di lakukan
# else:
#  sekenario terakhir
if nilai > 80:
    print("Selamat kamu lulus dari ujian")
else:
    print("Tidak lulus ujian")

# Singkat
# Tenery
print("=======Tenery=====")
pesan  = "Lulus" if nilai > 80 else "tidak lulus"
print(f"{pesan}")

# Conversi nilai
# >90 : A
# >80 : B
# >70 : C
# < 70 : E
# and (kondisi 1 dan kondisi 2 )
# or (kondisi 1 atau kondisi 2 )
print("===if elif else =====")
if nilai > 90 : 
    print("nilai kamu A")
elif nilai > 80 and nilai <= 90 :
    print("nilai kamu B")
elif nilai > 70 and nilai <= 80 :
    print("nilai kamu C")
else :
    print("nilai kamu E")

#switch
print("=====Switch=====")
print("=====Menu=======")
print("1. Start")
print("2. Exit")
select = input("Select => ")
match select:
    case "1":
        print("Start Game")
    case "2":
        print("See youu")
    case _ :
        print("Input not Valid")