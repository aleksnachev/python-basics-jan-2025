command = input()
sum_prime_numbers = 0
sum_non_prime_numbers = 0

while command != "stop":
    number = int(command)

    if number < 0:
        print("Number is negative.")
        command = input()
        continue

    is_it_prime = True
    w_counter = 0
    for w in range(1, number + 1):
        if number % w == 0:
            w_counter += 1

            if w_counter > 2:
                is_it_prime = False
                break

    if is_it_prime == True:
        sum_prime_numbers += number
    elif is_it_prime == False:
        sum_non_prime_numbers += number

    command = input()

print(f"Sum of all prime numbers is: {sum_prime_numbers}")
print(f"Sum of all non prime numbers is: {sum_non_prime_numbers}")
