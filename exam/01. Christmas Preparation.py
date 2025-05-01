wrapped_paper_count = int(input())
cloth_count = int(input())
glue_count = float(input())
percent = int(input())/100

wrapped_paper_price = wrapped_paper_count*5.8
cloth_price = cloth_count*7.2
glue_price = glue_count*1.2

needed_money = (1-percent)*(wrapped_paper_price+cloth_price+glue_price)

print(f"{(needed_money):.3f}")