# 	W - ако е победител получава 2000 точки
# 	F - ако е финалист получава 1200 точки
# 	SF - ако е полуфиналист получава 720 точки
import math
tournaments_count = int(input())
points = int(input())
winned_points = 0
winned_tournament = 0
for _ in range(tournaments_count):
    cur_position = input()

    if cur_position == "W":
        points += 2000
        winned_tournament+=1
        winned_points += 2000
    elif cur_position == "F":
        points += 1200
        winned_points += 1200
    elif cur_position == "SF":
        points+=720
        winned_points+=720

print(f"Final points: {points:.0f}")
average_points = math.floor(winned_points/tournaments_count)
print(f"Average points: {average_points}")
print(f"{(winned_tournament/tournaments_count*100):.2f}%")
