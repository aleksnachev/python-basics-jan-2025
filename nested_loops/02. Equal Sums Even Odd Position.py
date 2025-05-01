first_number = int(input())
second_number = int(input())

for number in range(first_number, second_number+1):
    number_to_str = str(number)
    # chetni
    sum_even = 0
    # nechetni
    sum_odd = 0

    for index, digit in enumerate(number_to_str):
        if index % 2 == 0:
            sum_even += int(digit)
        else:
            sum_odd += int(digit)

    if sum_even == sum_odd:
        print(number, end=" ")
