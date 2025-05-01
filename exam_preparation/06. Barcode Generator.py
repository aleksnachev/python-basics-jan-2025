start = int(input())
end = int(input())

start_str = str(start)
end_str = str(end)
start_num = int(start_str[0])
end_num = int(end_str[0])

start_num_2 = int(start_str[1])
end_num_2 = int(end_str[1])

start_num_3 = int(start_str[2])
end_num_3 = int(end_str[2])

start_num_4 = int(start_str[3])
end_num_4 = int(end_str[3])

for a in range(start_num, end_num + 1):
    if a % 2 == 0:
        continue
    for b in range(start_num_2, end_num_2 + 1):
        if b % 2 == 0:
            continue
        for c in range(start_num_3, end_num_3 + 1):
            if c % 2 == 0:
                continue
            for d in range(start_num_4, end_num_4 + 1):
                if d % 2 == 0:
                    continue
                print(f"{a}{b}{c}{d}", end=" ")
