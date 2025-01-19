excursion = float(input())
pazels = int(input())
tolking_doll = int(input())
teddy_bear = int(input())
petit_toy = int(input())
trucks = int(input())

discaunt = 0

total_toys = (pazels + tolking_doll + teddy_bear + petit_toy + trucks)
totoal_cost = (pazels * 2.60 + tolking_doll * 3 + teddy_bear * 4.10 + petit_toy * 8.20 + trucks * 2.00)

# проверка на условието за отстъпка и актуализация на отстъпката
if total_toys >= 50:
    discaunt = (totoal_cost * 0.25)
coast_whit_discount = (totoal_cost - discaunt)
rent = (coast_whit_discount * 0.1)
end_sum = (coast_whit_discount - rent)
# крайна сума
# Печат на резултата
if end_sum >= excursion:
    print(f"Yes! {abs(end_sum - excursion):.2f} lv left.")
else:
    print(f"Not enough money! {abs(end_sum - excursion):.2f} lv needed.")
