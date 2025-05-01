tshirt_price = float(input())
sum_for_free_ball = float(input())

shorts_price = 0.75*tshirt_price
socks_price = 0.2*shorts_price
boots_price = 2*(tshirt_price+shorts_price)

total_sum = (tshirt_price+socks_price+shorts_price+boots_price)*0.85


if total_sum >= sum_for_free_ball:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total_sum:.2f} lv.")
else:
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {(sum_for_free_ball-total_sum):.2f} lv. more.")



