juft = 0
toq = 0

for i in range(10):
    son = int(input("Son kiriting: "))
    if son % 2 == 0:
        juft += 1
    else:
        toq += 1

print("Juft sonlar:", juft, "ta")
print("Toq sonlar:", toq, "ta")





togri_parol = "0000"

for i in range(3):
    parol = input("Parolni kiriting: ")
    
    if parol == togri_parol:
        print("Xush kelibsiz!")
        break
    else:
        print("Parol noto'g'ri")
else:
    print("Kirish bloklandi")





son = int(input("Musbat son kiriting: "))

for i in range(1, son + 1):
    if son % i == 0:
        print(i)
