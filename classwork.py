sonlar = []

for i in range(5):
    son = int(input(f"{i+1}-sonni kiriting: "))
    sonlar.append(son)

eng_katta = sonlar[0]

for son in sonlar:
    if son > eng_katta:
        eng_katta = son

print("Eng gigant son:", eng_katta )





sonlar = []
for i in range(10):
    son = int(input(f"{i+1}-sonni kiriting: "))
    sonlar.append(son)

juft_soni = 0
toq_soni = 0

for son in sonlar:
    if son % 2 == 0:
        juft_soni += 1
    else:
        toq_soni += 1

print("Juft sonlar:", juft_soni, "ta")
print("Toq sonlar:", toq_soni, "ta")







togri_parol = "0000"

for urinish in range(3):
    parol = input("Parolni kiriting: ")
    
    if parol == togri_parol:
        print("Xush kelibsiz!")
        break
    else:
        print("Parol noto'g'ri")
else:
    print("Kirish bloklandi")






son = int(input(" sonni kiriting "))

for i in range(1, son + 1):
    if son % i == 0:
        print(i)
