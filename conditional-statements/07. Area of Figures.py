import math
figure = input()

if figure == "square":
    a = float(input())
    square = a*a
    print(f"{square:.3f}")
elif figure == "rectangle":
    a = float(input())
    b = float(input())
    square = a*b
    print(f"{square:.3f}")
elif figure == "circle":
    a = float(input())
    square = math.pi*a*a
    print(f"{square:.3f}")
elif figure == "triangle":
    a = float(input())
    b = float(input())
    square = a * b/2
    print(f"{square:.3f}")