width_apartment = int(input())
length_apartment = int(input())
height_apartment = int(input())
free_space = width_apartment*length_apartment*height_apartment

command = input()

while command!= "Done":

    step_space = int(command)
    free_space -= step_space

    if free_space<0:
        break

    command = input()

if free_space>=0:
    print(f"{free_space} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(free_space)} Cubic meters more.")