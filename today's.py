class Car:
    def __init__(self, model, rang, yili, narxi, tezligi):
        self.model = model
        self.rang = rang
        self.yili = yili
        self.narxi = narxi
        self.tezligi = tezligi

    def malumot(self):
        print(f"model: {self.model}")
        print(f"rang: {self.rang}")
        print(f"yili: {self.yili}")
        print(f"narxi: {self.narxi}")
        print(f"tezligi: {self.tezligi}")

    def fayl(self):
        with open("example.txt", "a") as f:
            f.write(f"model: {self.model}\n")
            f.write(f"rang: {self.rang}\n")
            f.write(f"yili: {self.yili}\n")
            f.write(f"narxi: {self.narxi}\n")
            f.write(f"tezligi: {self.tezligi}\n")
            f.write("--------------------\n")


while True:
    print("1 - Mashina qo'shish")
    print("2 - Mashina olish")
    print("3 - Chiqish")

    tanlov = input("Tanlang: ")

    if tanlov == "1":
        model = input("Model: ")
        rang = input("Rang: ")
        yili = input("Yili: ")
        narxi = input("Narxi: ")
        tezligi = input("Tezligi: ")

        mashina = Car(model, rang, yili, narxi, tezligi)
        mashina.malumot()
        mashina.fayl()
        print("saqlandi\n")

    elif tanlov == "2":
        qidiruv = input("Qaysi modelni qidiryapsiz: ")

        try:
            with open("example.txt", "r") as f:
                matn = f.read()

            if qidiruv in matn:
                print("\nTopildi:")
                print(matn)
            else:
                print("Bunday malmot topilmadi.\n")

    

    elif tanlov == "3":
        print("Dastur tugadi")
        break

    else:
        print("Noto'g'ri tanlov\n")
