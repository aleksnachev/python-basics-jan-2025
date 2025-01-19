
plastics = int(input())
paint = int(input())
water = int(input())
hours = int(input())

total_ammount_materials = (plastics+2)*1.5 + 1.1*paint*14.5 + water*5 + 0.4
total_workers = total_ammount_materials*0.3*hours
total = total_workers+total_ammount_materials

print(total)
