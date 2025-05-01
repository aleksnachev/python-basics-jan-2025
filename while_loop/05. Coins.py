change = float(input())
monets_count = 0
change_total = round(change * 100)

while True:
    if change_total // 200 >= 1:
        change_total -= 200
        monets_count += 1

    elif change_total // 100 >= 1:

        change_total -= 100
        monets_count += 1
    elif change_total // 50 >= 1:

        change_total -= 50
        monets_count += 1
    elif change_total // 20 >= 1:

        change_total -= 20
        monets_count += 1
    elif change_total // 10 >= 1:

        change_total -= 10
        monets_count += 1
    elif change_total // 5 >= 1:

        change_total -= 5
        monets_count += 1
    elif change_total // 2 >= 1:

        change_total -= 2
        monets_count += 1
    elif change_total // 1 >= 1:

        change_total -= 1
        monets_count += 1

    if change_total == 0:
        print(monets_count)
        break
