class Kutubxona:
    """Butun kutubxona tizimini boshqaruvchi asosiy klass"""

    MAX_KITOB = 3          
    PAROL = "0000"          

    def __init__(self):
        self.kitoblar = []      
        self.oquvchilar = {}   

   
    def tizimga_kirish(self):
        for urinish in range(3):   
            kiritilgan = input("Tizimga kirish uchun parolni kiriting: ")
            if kiritilgan == self.PAROL:
                print("Xush kelibsiz! Tizimga muvaffaqiyatli kirdingiz.\n")
                return True
            else:
                print("Parol noto'g'ri! Qayta urinib ko'ring.")
        print("3 marta xato urinish. Dastur to'xtatildi.")
        return False

    
    def kitob_qoshish(self, title, author):
        yangi_kitob = Book(title, author)
        self.kitoblar.append(yangi_kitob)
        print(f"Kitob qo'shildi: {yangi_kitob}")

   
    def oquvchi_qoshish(self, ism):
        if ism in self.oquvchilar:
            print(f"'{ism}' allaqachon ro'yxatda bor.")
        else:
            self.oquvchilar[ism] = []
            print(f"O'quvchi qo'shildi: {ism}")

    
    def kitob_topish(self, title):
        for kitob in self.kitoblar:
            if kitob.title.lower() == title.lower():
                return kitob
        return None

    
    def kitob_berish(self, oquvchi, title):
        if oquvchi not in self.oquvchilar:
            print(f"Xatolik: '{oquvchi}' degan o'quvchi ro'yxatda yo'q.")
            return

        kitob = self.kitob_topish(title)
        if kitob is None:
            print(f"Xatolik: '{title}' nomli kitob kutubxonada topilmadi.")
            return

        if kitob.status == "olingan":
            print(f"Xatolik: '{title}' kitobi hozir band, allaqachon olingan.")
            return

        if len(self.oquvchilar[oquvchi]) >= self.MAX_KITOB:
            print(f"Xatolik: {oquvchi} da allaqachon {self.MAX_KITOB} ta kitob bor.")
            return

        kitob.status = "olingan"
        self.oquvchilar[oquvchi].append(kitob)
        print(f"'{kitob.title}' kitobi {oquvchi} ga berildi.")

   
    def kitob_qaytarish(self, oquvchi, title):
        if oquvchi not in self.oquvchilar:
            print(f"Xatolik: '{oquvchi}' degan o'quvchi ro'yxatda yo'q.")
            return

        kitob = self.kitob_topish(title)
        if kitob is None or kitob not in self.oquvchilar[oquvchi]:
            print(f"Xatolik: {oquvchi} da '{title}' kitobi mavjud emas.")
            return

        kitob.status = "mavjud"
        self.oquvchilar[oquvchi].remove(kitob)
        print(f"'{kitob.title}' kitobi qaytarildi.")

    
    def kitoblarni_korish(self):
        if not self.kitoblar:
            print("Kutubxonada hozircha kitob yo'q.")
            return
        print("\n--- Kutubxonadagi kitoblar ---")
        for i, kitob in enumerate(self.kitoblar, start=1):
            print(f"{i}. {kitob}")
        print("-------------------------------\n")

    
    def oquvchilarni_korish(self):
        if not self.oquvchilar:
            print("Hozircha o'quvchi yo'q.")
            return
        print("\n--- O'quvchilar ro'yxati ---")
        for ism, kitoblar in self.oquvchilar.items():
            kitob_nomlari = ", ".join(k.title for k in kitoblar) if kitoblar else "hech narsa yo'q"
            print(f"- {ism}: {kitob_nomlari}")
        print("-------------------------------\n")



def main():
    kutubxona = Kutubxona()

    
    if not kutubxona.tizimga_kirish():
        return

    while True:
        print("===== KUTUBXONA MENEJER MENYUSI =====")
        print("1. Kitob qo'shish")
        print("2. O'quvchi qo'shish")
        print("3. Kitob berish")
        print("4. Kitob qaytarish")
        print("5. Barcha kitoblarni ko'rish")
        print("6. Barcha o'quvchilarni ko'rish")
        print("7. Chiqish")
        tanlov = input("Tanlovingizni kiriting (1-7): ")

        if tanlov == "1":
            title = input("Kitob nomi: ")
            author = input("Muallifi: ")
            kutubxona.kitob_qoshish(title, author)

        elif tanlov == "2":
            ism = input("O'quvchi ismi: ")
            kutubxona.oquvchi_qoshish(ism)

        elif tanlov == "3":
            oquvchi = input("O'quvchi ismi: ")
            title = input("Kitob nomi: ")
            kutubxona.kitob_berish(oquvchi, title)

        elif tanlov == "4":
            oquvchi = input("O'quvchi ismi: ")
            title = input("Kitob nomi: ")
            kutubxona.kitob_qaytarish(oquvchi, title)

        elif tanlov == "5":
            kutubxona.kitoblarni_korish()

        elif tanlov == "6":
            kutubxona.oquvchilarni_korish()

        elif tanlov == "7":
            print("Dasturdan chiqildi. Xayr!")
            break

        else:
            print("Noto'g'ri tanlov! 1-7 orasida son kiriting.")

        print()  


if __name__ == "__main__":
    main()

class Kitob:
    def __init__(self, nomi):
        self.nomi = nomi
        self.holati = "mavjud"   
        self.egasi = None           


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































class Order:
    def __init__(self):
        self.items = []  # (nomi, narxi, soni)

    def taom_qoshish(self, nomi, narxi, soni=1):
        self.items.append({"nomi": nomi, "narxi": narxi, "soni": soni})
        print(f"{nomi} savatga qo'shildi.")

    def summa_hisoblash(self):
        return sum(item["narxi"] * item["soni"] for item in self.items)

    def yakuniy_hisob(self):
        summa = self.summa_hisoblash()

        if summa >= 100000:
            yetkazib_berish = 0
        else:
            yetkazib_berish = 15000

        jami = summa + yetkazib_berish

        print(f"Taomlar summasi: {summa} so'm")
        print(f"Yetkazib berish: {yetkazib_berish} so'm")
        print(f"Jami to'lov: {jami} so'm")
        return jami


order = Order()
order.taom_qoshish("Osh", 35000, 2)
order.taom_qoshish("Salat", 15000, 1)

order.yakuniy_hisob()
