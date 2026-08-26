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
