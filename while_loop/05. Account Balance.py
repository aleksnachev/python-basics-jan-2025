sum = 0

while True:
    data = input()
    if data == "NoMoreMoney":
        break
    cur_sum = float(data)

    if cur_sum >= 0:
        sum += cur_sum
        print(f"Increase: {cur_sum:.2f}")
    else:
        print("Invalid operation!")
        break

print(f"Total: {sum:.2f}")
