length = int(input())
width = int(input())
cake_total_pieces = length*width

command = input()
while command != "STOP":
    cur_pieces = int(command)
    cake_total_pieces-= cur_pieces

    if cake_total_pieces<=0:
        break
    command = input()

if cake_total_pieces>0:
    print(f"{cake_total_pieces} pieces are left.")
else:
    print(f"No more cake left! You need {abs(cake_total_pieces)} pieces more.")