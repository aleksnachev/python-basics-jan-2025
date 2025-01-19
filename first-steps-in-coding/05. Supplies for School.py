

pens = int(input())
markers = int(input())
sprays = int(input())
percent = int(input())/100

total_ammount = (pens*5.8 + markers*7.2 + sprays*1.2)* (1-percent)
print(total_ammount)