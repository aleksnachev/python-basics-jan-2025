length = int(input())
width = int(input())
height = int(input())
percent_not_empty = float(input())/100

total_volume = length*width*height
total_volume_in_liters=total_volume/1000

liters_needed = total_volume_in_liters*(1-percent_not_empty)
print(liters_needed)