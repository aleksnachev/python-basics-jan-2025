needed_money = float(input())
money = float(input())
spend_counter = 0
days_counter = 0

while True:
    command = input()
    sum_command = float(input())
    days_counter += 1

    if command == "save":
        money += sum_command
        spend_counter = 0
    else:
        if sum_command >= money:
            money = 0
        else:
            money = money - sum_command

        spend_counter += 1

        if spend_counter == 5:
            print("You can't save the money.")
            print(days_counter)
            break

    if money >= needed_money:
        print(f"You saved the money for {days_counter} days.")
        break
