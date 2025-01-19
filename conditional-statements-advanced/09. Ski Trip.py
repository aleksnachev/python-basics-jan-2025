
# вид помещение	            по-малко от 10 дни	            между 10 и 15 дни	                повече от 15 дни
# room for one person	    не ползва намаление	            не ползва намаление	                не ползва намаление
# apartment	                30% от крайната цена	        35% от крайната цена	            50% от крайната цена
# president apartment	    10% от крайната цена	        15% от крайната цена	            20% от крайната цена

# 	"room for one person" – 18.00 лв за нощувка
# 	"apartment" – 25.00 лв за нощувка
# 	"president apartment" – 35.00 лв за нощувка


days = int(input())
room = input()
feedback = input()

nights = days-1
total_price=0

if room == "room for one person":

    total_price = 18*nights
elif room == "apartment":

    total_price = 25*nights
    if days<10:
        total_price*=0.7
    elif days<=15:
        total_price*=0.65
    else:
        total_price*=0.5

elif room == "president apartment":

    total_price = 35 * nights
    if days < 10:
        total_price *= 0.9
    elif days <= 15:
        total_price *= 0.85
    else:
        total_price *= 0.8


if feedback == "positive":
    total_price*=1.25
else:
    total_price*=0.9

print(f"{total_price:.2f}")