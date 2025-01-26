# •	Група до 5 човека – изкачват Мусала
# •	Група от 6 до 12 човека – изкачват Монблан
# •	Група от 13 до 25 човека – изкачват Килиманджаро
# •	Група от 26 до 40 човека –  изкачват К2
# •	Група от 41 или повече човека – изкачват Еверест

groups = int(input())
all_people = 0
musala = 0
monblan = 0
kilimandzaro = 0
k2 = 0
everest = 0

for _ in range(groups):
    group_number = int(input())

    if group_number <= 5:
        musala += group_number
    elif 6 <= group_number <= 12:
        monblan += group_number
    elif 13 <= group_number <= 25:
        kilimandzaro += group_number
    elif 26 <= group_number <= 40:
        k2 += group_number
    elif group_number >= 41:
        everest += group_number

    all_people += group_number

musala_percent = musala / all_people * 100
monblan_percent = monblan / all_people * 100
kilimandzaro_percent = kilimandzaro / all_people * 100
k2_percent = k2 / all_people * 100
everest_percent = everest / all_people * 100

print(f"{musala_percent:.2f}%")
print(f"{monblan_percent:.2f}%")
print(f"{kilimandzaro_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{everest_percent:.2f}%")
