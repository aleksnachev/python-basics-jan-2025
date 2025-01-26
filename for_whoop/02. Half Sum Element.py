import sys

n = int(input())
max_num = - sys.maxsize
sum = 0

for i in range(n):
    num = int(input())
    if num>max_num:
        max_num = num

    sum += num

if max_num == sum - max_num:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    sum = sum-max_num
    print("No")
    print(f"Diff = {abs(max_num-sum)}")