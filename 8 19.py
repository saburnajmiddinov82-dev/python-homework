


class Kutubxona:
    parol = "0000"

    def __init__(self):
        self.kitoblar = []   

    def kitob_qoshish(self, nomi):
        yangi = Kitob(nomi)
        self.kitoblar.append(yangi)
        print(f"'{nomi}' kitobi qo'shildi.")

    def kitob_berish(self, oquvchi, nomi):
      
        soni = 0
        for k in self.kitoblar:
            if k.egasi == oquvchi:
                soni += 1

        if soni >= 3:
            print(f"Xatolik: {oquvchi} da allaqachon 3 ta kitob bor.")
            return

        
        for k in self.kitoblar:
            if k.nomi == nomi:
                if k.holati == "olingan":
                    print(f"Xatolik: '{nomi}' kitobi band.")
                    return
                k.holati = "olingan"
                k.egasi = oquvchi
                print(f"'{nomi}' kitobi {oquvchi} ga berildi.")
                return

        print(f"Xatolik: '{nomi}' kitob topilmadi.")

    def kitob_qaytarish(self, oquvchi, nomi):
        for k in self.kitoblar:
            if k.nomi == nomi and k.egasi == oquvchi:
                k.holati = "mavjud"
                k.egasi = None
                print(f"'{nomi}' kitobi qaytarildi.")
                return
        print(f"Xatolik: {oquvchi} da '{nomi}' kitobi yo'q.")

    def korish(self):
        if not self.kitoblar:
            print("Kitoblar yo'q.")
            return
        for k in self.kitoblar:
            if k.holati == "olingan":
                print(f"{k.nomi} - {k.holati} ({k.egasi})")
            else:
                print(f"{k.nomi} - {k.holati}")



kutubxona = Kutubxona()

parol = input("parolni kiriting: ")
if parol != Kutubxona.parol:
    print("parol xato.")
else:
    while True:
        print("\n1-Kitob qoshish  2-Kitob berish  3-Kitob qaytarish  4-Korish  5-Chiqish")
        tanlov = input("tanlov: ")

        if tanlov == "1":
            nomi = input("Kitob nomi: ")
            kutubxona.kitob_qoshish(nomi)

        elif tanlov == "2":
            oquvchi = input("Oquvchi ismi: ")
            nomi = input("Kitob nomi: ")
            kutubxona.kitob_berish(oquvchi, nomi)

        elif tanlov == "3":
            oquvchi = input("Oquvchi ismi: ")
            nomi = input("Kitob nomi: ")
            kutubxona.kitob_qaytarish(oquvchi, nomi)

        elif tanlov == "4":
            kutubxona.korish()

        elif tanlov == "5":
            print("Xayr!")
            break

        else:
            print("Notogri tanlov!")
