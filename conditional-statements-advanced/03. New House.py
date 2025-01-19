# цвете	                Роза	Далия	Лале	Нарцис	Гладиола
# Цена на брой в лева	   5	 3.80	2.80	3	    2.50

# •	Ако Нели купи повече от 80 Рози - 10% отстъпка от крайната цена;
# •	Ако Нели купи повече от 90  Далии - 15% отстъпка от крайната цена;
# •	Ако Нели купи повече от 80 Лалета - 15% отстъпка от крайната цена;
# •	Ако Нели купи по-малко от 120 Нарциса - цената се оскъпява с 15%;
# •	Ако Нели Купи по-малко от 80 Гладиоли - цената се оскъпява с 20%.

# "Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus";

flower = input()
quantity = int(input())
budget = int(input())
total_sum = 0

if flower == "Roses":

    if quantity > 80:
        total_sum = quantity * 5 * 0.9
    else:
        total_sum = quantity * 5

elif flower == "Dahlias":

    if quantity > 90:
        total_sum = quantity * 3.8 * 0.85
    else:
        total_sum = quantity * 3.8

elif flower == "Tulips":

    if quantity > 80:
        total_sum = quantity * 2.8 * 0.85
    else:
        total_sum = quantity * 2.8

elif flower == "Narcissus":

    if quantity < 120:
        total_sum = quantity * 3 * 1.15
    else:
        total_sum = quantity * 3

elif flower == "Gladiolus":

    if quantity < 80:
        total_sum = quantity * 2.5 * 1.2
    else:
        total_sum = quantity * 2.5

if budget >= total_sum:
    print(f"Hey, you have a great garden with {quantity} {flower} and {budget-total_sum:.2f} leva left.")
else:
    print(f"Not enough money, you need {total_sum-budget:.2f} leva more.")
