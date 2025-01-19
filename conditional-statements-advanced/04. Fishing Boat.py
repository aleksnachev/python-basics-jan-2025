# В зависимост от сезона:
# •	Цената за наем на кораба през пролетта е  3000 лв.;
# •	Цената за наем на кораба през лятото и есента е  4200 лв.;
# •	Цената за наем на кораба през зимата е  2600 лв.
#
# В зависимост от броя на групата има различна отстъпка:
# •	Ако групата е до 6 човека включително  -  отстъпка от 10%;
# •	Ако групата е от 7 до 11 човека включително  -  отстъпка от 15%;
# •	Ако групата е от 12 нагоре  -  отстъпка от 25%.
# 5% отстъпка, ако са четен брой, освен ако не е есен - тогава нямат допълнителна отстъпка, която се начислява след като се приспадне отстъпката по горните критерии.
# Напишете програма, която да пресмята дали рибарите ще съберат достатъчно пари.

# : "Spring", "Summer", "Autumn" или "Winter";
budget = int(input())
season = input()
quantity_fishermans = int(input())
total_sum = 0

if season == "Spring":

    total_sum += 3000
    if quantity_fishermans <= 6:
        total_sum *= 0.9
    elif quantity_fishermans <= 11:
        total_sum *= 0.85
    else:
        total_sum *= 0.75

    if quantity_fishermans % 2 == 0:
        total_sum *= 0.95

elif season == "Summer":

    total_sum += 4200
    if quantity_fishermans <= 6:
        total_sum *= 0.9
    elif quantity_fishermans <= 11:
        total_sum *= 0.85
    else:
        total_sum *= 0.75

    if quantity_fishermans % 2 == 0:
        total_sum *= 0.95

elif season == "Autumn":

    total_sum += 4200
    if quantity_fishermans <= 6:
        total_sum *= 0.9
    elif quantity_fishermans <= 11:
        total_sum *= 0.85
    else:
        total_sum *= 0.75

elif season == "Winter":

    total_sum += 2600
    if quantity_fishermans <= 6:
        total_sum *= 0.9
    elif quantity_fishermans <= 11:
        total_sum *= 0.85
    else:
        total_sum *= 0.75

    if quantity_fishermans % 2 == 0:
        total_sum *= 0.95

if budget >= total_sum:
    print(f"Yes! You have {budget - total_sum:.2f} leva left.")
else:
    print(f"Not enough money! You need {total_sum - budget:.2f} leva.")
