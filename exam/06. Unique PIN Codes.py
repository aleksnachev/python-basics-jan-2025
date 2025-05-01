end_1_num = int(input())
end_2_num = int(input())
end_3_num = int(input())

for a in range(1,end_1_num+1):
    if a %2!=0:
        continue
    for b in range(1,end_2_num+1):
        if b != 2 and b != 3 and b != 5 and b != 7:
            continue
        for c in range(1, end_3_num + 1):
            if c % 2 != 0:
                continue
            print(f"{a} {b} {c}")
