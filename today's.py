class Car:
    def __init__(self, model, rang, yili, narxi, tezligi):
        self.model = model
        self.rang = rang
        self.yili = yili
        self.narxi = narxi
        self.tezligi = tezligi

    def saqla(self):
        file = open("mashinalar.txt", "a")
        file.write(f"{self.model},{self.rang},{self.yili},{self.narxi},{self.tezligi}\n")
        file.close()


while True:
    print("\n1. Mashina qo'shish")
    print("2. Mashinalarni ko'rish")
    print("3. Chiqish")

    tanlov = input("Tanlang: ")

    if tanlov == "1":
        model = input("Model: ")
        rang = input("Rang: ")
        yili = input("Yili: ")
        narxi = input("Narxi: ")
        tezligi = input("Tezligi: ")

        mashina = Car(model, rang, yili, narxi, tezligi)
        mashina.saqla()

        print("Saqlandi!")

    elif tanlov == "2":
        file = open("mashinalar.txt", "r")

        for mashina in file:
            print(mashina.strip())

        file.close()

    elif tanlov == "3":
        break

    else:
        print("Noto'g'ri tanlov!")
