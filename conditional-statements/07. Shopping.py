budget = float(input())
number_video_cards = int(input())
number_processors = int(input())
number_ram = int(input())

video_cards = number_video_cards * 250
processor = 0.35 * video_cards * number_processors
ram = 0.1 * video_cards * number_ram

total = video_cards + processor + ram

if number_video_cards > number_processors:
    total *= 0.85

if budget >= total:
    print(f"You have {(budget - total):.2f} leva left!")
else:
    print(f"Not enough money! You need {(total - budget):.2f} leva more!")
