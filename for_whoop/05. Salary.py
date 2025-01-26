# Facebook" -> 150 лв.
# •	"Instagram" -> 100 лв.
# •	"Reddit" -> 50 лв.

n = int(input())
salary = float(input())

for _ in range(n):
    app = input()

    if app == "Facebook":
        salary -= 150
    elif app == "Instagram":
        salary -= 100
    elif app == "Reddit":
        salary -= 50

    if salary>0:
        continue
    else:
        print("You have lost your salary.")
        break
else:
    print(f"{salary:.0f}")