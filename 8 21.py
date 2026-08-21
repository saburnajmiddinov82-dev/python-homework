8kvadrat = lambda son: son ** 2
print("1-natija:", kvadrat(5))



a = 15
b = 23
kattasi = lambda a, b: a if a > b else b
print("2-natija:", kattasi(a, b))



sonlar = [2, 4, 6, 8, 10]
natija3 = list(map(lambda x: x * 3, sonlar))
print("3-natija:", natija3)



ismlar = ["ali", "vali", "sardor", "bobur"]
natija4 = list(map(lambda ism: ism.upper(), ismlar))
print("4-natija:", natija4)
