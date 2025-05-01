command = input()
tickets_counter = 0
student_counter = 0
standard_counter = 0
kid_counter = 0

while command != "Finish":
    name_movie = command
    free_space = int(input())
    purchased_tickets = 0

    while free_space > 0:
        ticket_type = input()
        if ticket_type == "End":
            break
        elif ticket_type == "student":
            student_counter += 1
        elif ticket_type == "standard":
            standard_counter += 1
        elif ticket_type == "kid":
            kid_counter += 1

        tickets_counter += 1
        purchased_tickets += 1
        free_space -= 1

    print(f"{name_movie} - {(purchased_tickets / (purchased_tickets + free_space) * 100):.2f}% full.")

    command = input()


if tickets_counter > 0:
    student_percent = (student_counter / tickets_counter) * 100
    standard_percent = (standard_counter / tickets_counter) * 100
    kid_percent = (kid_counter / tickets_counter) * 100
else:
    student_percent = standard_percent = kid_percent = 0

print(f"Total tickets: {tickets_counter}")
print(f"{student_percent:.2f}% student tickets.")
print(f"{standard_percent:.2f}% standard tickets.")
print(f"{kid_percent:.2f}% kids tickets.")

