price_strawberries = float(input())
kg_bananas = float(input())
kg_oranges = float(input())
kg_raspberry=float(input())
kg_strawberries = float(input())

price_raspberry = price_strawberries/2
price_oranges = 0.6*price_raspberry
price_bananas = 0.2*price_raspberry

price2_strawberries = round(price_strawberries * kg_strawberries,2)


needed_money =price_bananas*kg_bananas+price_oranges*kg_oranges+price2_strawberries+price_raspberry*kg_raspberry
print(round(needed_money,2))



