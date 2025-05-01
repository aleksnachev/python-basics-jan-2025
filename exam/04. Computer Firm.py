n = int(input())
reating_sum = 0
all_sales = 0
sales = 0


for k in range(n):
    num = str(input())
    reating_now = int(num[2])
    reating_sum+=reating_now
    possible_sales = int(num[0]+num[1])
    all_sales+=possible_sales

    if reating_now == 2:
        possible_sales = 0
    elif reating_now == 3:
        possible_sales *= 0.5
    elif reating_now == 4:
        possible_sales *= 0.7
    elif reating_now == 5:
        possible_sales *= 0.85
    elif reating_now == 6:
        possible_sales *= 1

    sales+=possible_sales

print(f"{sales:.2f}")
print(f"{(reating_sum/n):.2f}")



