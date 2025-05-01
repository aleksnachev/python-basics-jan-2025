sea_vacations_count = int(input())
mountain_vacations_count = int(input())
command = input()
total_sum = 0

while command != "Stop":

    if command == "sea" and sea_vacations_count > 0:
        total_sum+=680
        sea_vacations_count-=1
    elif command == "mountain" and mountain_vacations_count >0:
        total_sum+=499
        mountain_vacations_count-=1

    if sea_vacations_count==0 and mountain_vacations_count == 0:
        print("Good job! Everything is sold.")
        break

    command = input()

print(f"Profit: {total_sum} leva.")


