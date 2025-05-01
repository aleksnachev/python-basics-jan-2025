goal = 10000
steps_total = 0

while True:
    command = input()

    if command == "Going home":
        plus_steps = int(input())
        steps_total+=plus_steps

        if steps_total>= goal:
            print("Goal reached! Good job!")
            print(f"{steps_total-goal} steps over the goal!")
            break
        else:
            print(f"{goal-steps_total} more steps to reach goal.")
            break
    else:
        steps_now = int(command)
        steps_total+=steps_now
        if steps_total>= goal:
            print("Goal reached! Good job!")
            print(f"{steps_total-goal} steps over the goal!")
            break

