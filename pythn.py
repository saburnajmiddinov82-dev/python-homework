jurnal = {}   

for i in range(5):
    ism = input("O'quvchi ismini kiriting: ")
    jurnal[i] = ism   
print("Sinf jurnali:")parol = input("Parolni kiriting")
login = input("Loginni kiriting")

if login == "omad" and parol == "0000":
    print("Xush kordik")
else:
    print("Login yoki parol notogri iltimos tekshrib ko'ring")

    kino uchu  yoshh####################################

yosh = int(input("Yoshingizni kiriting: "))

if yosh >= 13:
    print("Ko'rishingiz mumkun")

else:
    print("Avval 13 yoshtan oshing" )

#####vazifa chegirmmaaa#########################

summa = float(input("summani kiriting: "))

if summa >= 500000:
    yakuniy_narx = summa - (summa * 0.10)
    print("Chegirma qo'llanildi. Yakuniy narx:", yakuniy_narx)
else:
    print("Asl narxi:", summa)
##vazifaaaaaa############################

foiz = int(input("Batareya foizini kiriting: "))

if foiz < 20:
    print("Tezzz zaryadlang hoz ochadi tel")
elif foiz <= 80:
    print("Zaryad normal")
else:
    print("Zaryadka deyarli tolaa")
for raqam, ism in jurnal.items():
    print(raqam + 1, "-", ism)


parol = input("Parolni kiriting: ")

if len(parol) < 8:
    print("Parol qisqa")
else:
    print("kirishingiz mumkun")



soni = int(input("Nechta mahsulot sotib olasiz: "))

savat = []

for i in range(soni):
    mahsulot = input("Mahsulot nomini kiriting: ")
    savat.append(mahsulot)

print("Sizning savatingiz:")
for mahsulot in savat:
    print("-", mahsulot)


xabar = input("Xabaringizni kiriting: ")

soni = xabar.count("/")

print("Belgi soni:", soni)


ismlar = []

for i in range(5):
    ism = input("Ism kiriting: ")
    ismlar.append(ism)

yangi_ism = input("QIDIRUV ismini kiriting: ")

if yangi_ism in ismlar:
    print("Topildi")
else:
    print("Topilmadi")




soni = int(input("Mehmonlar sonini kiriting: "))

mehmonlar = []

for i in range(soni):
    ism = input("Mehmon ismini kiriting: ")
    mehmonlar.append(ism)

print("Jami mehmonlar soni:", soni)
print("Birinchi mehmon ismi:", mehmonlar[0])
print("Oxirgi mehmon ismi:", mehmonlar[-1])
