class Kutubxona:
    def __init__(self, kitoblar_soni=0):
        self.kitoblar_soni = kitoblar_soni

    def kitob_qoshish(self, soni):
        self.kitoblar_soni += soni
        print(f"{soni} ta kitob kutubxonaga qo'shildi.")

    def holat(self):
        print(f"Kutubxonada jami: {self.kitoblar_soni} ta kitob bor")

    def kitob_berish(self, soni):
        if soni <= self.kitoblar_soni:
            self.kitoblar_soni -= soni
            print(f"{soni} ta kitob o'quvchiga berildi.")
        else:
            print("Yetarli kitob yo'q.")

    def kitob_qaytarish(self, soni):
        self.kitoblar_soni += soni
        print(f"{soni} ta kitob qaytarildi.")


parol = "5678"
kutubxona = Kutubxona()

while True:
    passw = input(" parol ")

    if passw == parol:
        while True:
            print("\nQays amalni bajarasiz?")
            print("1. kitob qoshish")
            print("2. kitoblar sonini ko'rish")
            print("3. kitob berish")
            print("4. kitob qaytarish")
            print("5. Chiqish")

            choice = input("Amalni tanlang: ")

            if choice == "1":
                soni = int(input("Nechta kitob qoshmoqchisiz: "))
                kutubxona.kitob_qoshish(soni)

            elif choice == "2":
                kutubxona.holat()

            elif choice == "3":
                soni = int(input("Nechta kitob bermoqchisiz: "))
                kutubxona.kitob_berish(soni)

            elif choice == "4":
                soni = int(input("Nechta kitob qaytarilmoqchi: "))
                kutubxona.kitob_qaytarish(soni)

            elif choice == "5":
                print("Dastur tugadi.")
                break

            else:
                print("Notogri tanlov!")

        break

    else:
        print("Parol notog'ri!")
