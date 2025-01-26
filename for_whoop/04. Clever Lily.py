age_lili = int(input())
washing_machine_price = float(input())
toy_price_p = int(input())

sum = 0

for year in range(1,age_lili+1):

    if year%2==0:
        sum += year/2*10 - 1
    else:
        sum += toy_price_p

if sum>= washing_machine_price:
    print(f"Yes! {(sum-washing_machine_price):.2f}" )
else:
    print(f"No! {(washing_machine_price-sum):.2f}" )