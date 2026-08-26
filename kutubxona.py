



class Order:
    def __init__(self):
        self.items = [] 

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
