from math import ceil

serial_name = input()
duration_episode = int(input())
duration_lunch = int(input())

lunch_time = duration_lunch / 8
break_time = duration_lunch / 4

time_left = duration_lunch - (duration_episode + lunch_time + break_time)

if time_left >= 0:
    print(f"You have enough time to watch {serial_name} and left with {ceil(time_left)} minutes free time.")
else:
    print(f"You don't have enough time to watch {serial_name}, you need {ceil(abs(time_left))} more minutes.")
