film = input()
r = int(input())
c = int(input())
price = 0

# •	Premiere - премиерна прожекция, на цена 12.00 лева;
# •	Normal - стандартна прожекция, на цена 7.50 лева;
# •	Discount - прожекция за деца, ученици и студенти на намалена цена от 5.00 лева.

if film == "Premiere":
    price = 12
elif film == "Normal":
    price = 7.5
elif film == "Discount":
    price = 5

final_price = r*c*price

print(f"{final_price:.2f} leva")

