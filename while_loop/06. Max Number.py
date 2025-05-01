import sys

max_num = -sys.maxsize
while True:
    command = input()

    if command == "Stop":
        break

    cur_num = int(command)
    if cur_num>max_num:
        max_num = cur_num

print(max_num)