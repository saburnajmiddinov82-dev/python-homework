class Book:
    """Bitta kitobni ifodalaydigan klass"""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.status = "mavjud"   

    def __str__(self):
        return f"'{self.title}' - {self.author} ({self.status})"


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
