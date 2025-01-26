name_actor = input()
points = float(input())
n = int(input())

for i in range(n):
    name_critic = input()
    points_critic = float(input())
    points += (len(name_critic)*points_critic)/2

    if points>1250.5:
        print(f"Congratulations, {name_actor} got a nominee for leading role with {points:.1f}!")
        break

else:
    print(f"Sorry, {name_actor} you need {(1250.5-points):.1f} more!")
