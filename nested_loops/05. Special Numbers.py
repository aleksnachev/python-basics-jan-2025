n = int(input())

for number in range(1111, 10000):
    number_to_str = str(number)
    is_special = True

    for char in number_to_str:
        char_as_num = int(char)

        if char_as_num == 0:
            is_special = False
            break

        if n % char_as_num != 0:
            is_special = False
            break

    if is_special:
        print(number, end=" ")
