budget_film = float(input())
destination = input()
season = input()
days = int(input())
total_sum = 0

# Дестинация
# Сезон	     Dubai	    Sofia	    London
# Winter	45 000 lv.	17 000 lv.	24 000 lv.
# Summer	40 000 lv.	12 500 lv.	20 250 lv.
if season == "Winter":
    if destination == "Dubai":
        total_sum = 45000*days*0.7
    elif destination == "Sofia":
        total_sum = 17000*days*1.25
    elif destination == "London":
        total_sum = 24000*days
elif season == "Summer":
    if destination == "Dubai":
        total_sum = 40000*days*0.7
    elif destination == "Sofia":
        total_sum = 12500*days*1.25
    elif destination == "London":
        total_sum = 20250*days

if total_sum<=budget_film:
    print(f"The budget for the movie is enough! We have {(budget_film-total_sum):.2f} leva left!")
else:
    print(f"The director needs {(total_sum-budget_film):.2f} leva more!")


