egs_one = int(input())
egs_two = int(input())
command = input()
flag = False


while command!="End":

    if command == "one":
        egs_two-=1
    else:
        egs_one-=1

    if egs_one == 0:
        print(f"Player one is out of eggs. Player two has {egs_two} eggs left.")
        flag = True
        break
    elif egs_two == 0:
        print(f"Player two is out of eggs. Player one has {egs_one} eggs left.")
        flag = True
        break

    command=input()

if flag == False:
    print(f"Player one has {egs_one} eggs left.")
    print(f"Player two has {egs_two} eggs left.")
