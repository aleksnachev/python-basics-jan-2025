# Магазин за плодове през работните дни работи на следните цени:
#
# плод    banana  apple   orange  grapefruit  kiwi    pineapple   grapes
#
# цена    2.50    1.20    0.85    1.45        2.70     5.50       3.85

# През събота и неделя магазинът работи на по-високи цени:
#
# плод  banana  apple   orange  grapefruit  kiwi    pineapple   grapes
#
# цена  2.70    1.25    0.90    1.60        3.00    5.60        4.20\

fruit = input()
day_of_week = input()
quantity = float(input())


if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" or day_of_week == "Thursday" or day_of_week == "Friday":

    if fruit == "banana":
        print(f"{quantity*2.5:.2f}")
    elif fruit == "apple":
        print(f"{quantity*1.2:.2f}")
    elif fruit == "orange":
        print(f"{quantity*0.85:.2f}")
    elif fruit == "grapefruit":
        print(f"{quantity*1.45:.2f}")
    elif fruit == "kiwi":
        print(f"{quantity*2.7:.2f}")
    elif fruit == "pineapple":
        print(f"{quantity*5.5:.2f}")
    elif fruit == "grapes":
        print(f"{quantity*3.85:.2f}")
    else:
        print("error")
elif day_of_week == "Saturday" or day_of_week == "Sunday":
    if fruit == "banana":
        print(f"{quantity*2.7:.2f}")
    elif fruit == "apple":
        print(f"{quantity*1.25:.2f}")
    elif fruit == "orange":
        print(f"{quantity*0.9:.2f}")
    elif fruit == "grapefruit":
        print(f"{quantity*1.6:.2f}")
    elif fruit == "kiwi":
        print(f"{quantity*3:.2f}")
    elif fruit == "pineapple":
        print(f"{quantity*5.6:.2f}")
    elif fruit == "grapes":
        print(f"{quantity*4.2:.2f}")
    else:
        print("error")

else:
    print("error")

