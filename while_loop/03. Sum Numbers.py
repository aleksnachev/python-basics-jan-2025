number = int(input())
sum_numbers = 0

while True:
    cur_num = int(input())
    sum_numbers += cur_num

    if sum_numbers >= number:
        print(sum_numbers)
        break
