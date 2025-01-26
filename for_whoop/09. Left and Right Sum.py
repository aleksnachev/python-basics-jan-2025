n = int(input())*2
left_sum = 0
right_sum = 0

for char in range(n):
    cur_num=int(input())

    if char<n/2:
        left_sum+=cur_num
    else:
        right_sum+=cur_num

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {abs(left_sum-right_sum)}")
