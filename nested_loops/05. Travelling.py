command = input()
while command != "End":
    destination = ""
    required_budget = 0
    sum = 0
    if type(command) == str:
        destination = command
        required_budget = float(input())

        while sum < required_budget or type(command) != str:
            now_sum = float(input())
            sum += now_sum

            if sum >= required_budget:
                print(f"Going to {destination}!")
                break
    command = input()
