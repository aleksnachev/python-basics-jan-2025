import sys

min_num = sys.maxsize
while True:
    command = input()

    if command == "Stop":
        break

    cur_num = int(command)
    if cur_num<min_num:
        min_num = cur_num

print(min_num)