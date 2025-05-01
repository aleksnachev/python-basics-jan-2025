budget = float(input())
nights_count = int(input())
night_price = float(input())
extra_fees_percent = int(input())/100
total_sum = 0

if nights_count>7:
    night_price = 0.95*night_price

total_sum+= night_price*nights_count
extra_fees = extra_fees_percent*budget
total_sum+=extra_fees

if total_sum<=budget:
    print(f"Ivanovi will be left with {(budget-total_sum):.2f} leva after vacation.")
else:
    print(f"{(total_sum-budget):.2f} leva needed.")