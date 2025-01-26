number = int(input())
odd_sum = 0
even_sum = 0

for index in range(number):
    current_num = int(input())

    if index%2==0:
        even_sum+=current_num
    else:
        odd_sum+=current_num

if even_sum==odd_sum:
    print('Yes')
    print(f"Sum = {odd_sum}")
else:
    print("No")
    print(f"Diff = {abs(odd_sum-even_sum)}")