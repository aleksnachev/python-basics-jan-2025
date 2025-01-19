# Бюджетът определя дестинацията, а сезонът - колко от бюджета ще изхарчи. Ако е лято ще почива на къмпинг, а зимата в хотел. Ако е в Европа, независимо от сезона, ще почива в хотел.
# Всеки къмпинг или хотел, според дестинацията, има собствена цена, която отговаря на даден процент от бюджета:
# •	При 100 лв. или по-малко - някъде в България:
# o	Лято - 30% от бюджета;
# o	Зима - 70% от бюджета.
# •	При 1000 лв. или по малко - някъде на Балканите:
# o	Лято - 40% от бюджета;
# o	Зима - 80% от бюджета.
# •	При повече от 1000 лв. - някъде из Европа:
# o	При пътуване из Европа, независимо от сезона, ще похарчи 90% от бюджета.
# "summer” или "winter”
budget = float(input())
season = input()
total_sum=0
destination = ""
type_vacation=""
# Bulgaria", "Balkans" и "Europe"

if season == "summer":

    if budget>1000:
        destination = "Europe"
        type_vacation = "Hotel"
        total_sum = 0.9*budget
    elif 1000>=budget>100:
        destination = "Balkans"
        type_vacation = "Camp"
        total_sum = 0.4*budget
    elif 100>=budget:
        destination = "Bulgaria"
        type_vacation = "Camp"
        total_sum = 0.3*budget
elif season == "winter":

    if budget>1000:
        destination = "Europe"
        type_vacation = "Hotel"
        total_sum = 0.9*budget
    elif 1000>=budget>100:
        destination = "Balkans"
        type_vacation = "Hotel"
        total_sum = 0.8*budget
    elif 100>=budget:
        destination = "Bulgaria"
        type_vacation = "Hotel"
        total_sum = 0.7*budget

print(f"Somewhere in {destination}")
print(f"{type_vacation} - {total_sum:.2f}")


