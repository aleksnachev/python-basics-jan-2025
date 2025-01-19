budget = float(input())
statists = int(input())
price_per_statist = float(input())

decor = 0.1 * budget
clothes = statists * price_per_statist

if statists > 150:
    clothes *= 0.9

needed_money = decor + clothes

if needed_money > budget:
    print("Not enough money!")
    print(f"Wingard needs {needed_money - budget:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {budget - needed_money:.2f} leva left.")
