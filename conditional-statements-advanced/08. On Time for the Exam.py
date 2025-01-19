hour_exam = int(input())
minutes_exam = int(input())
hour_arrive = int(input())
minutes_arrive = int(input())

# Изчисляване на общите минути за часа на изпита и пристигането
all_minutes_exam = hour_exam * 60 + minutes_exam
all_minutes_arrive = hour_arrive * 60 + minutes_arrive

# Изчисляване на разликата в минутите
difference = all_minutes_arrive - all_minutes_exam

if difference > 0:  # Студентът е закъснял
    print("Late")
    if difference < 60:
        print(f"{difference} minutes after the start")
    else:
        hours = difference // 60
        minutes = difference % 60
        print(f"{hours}:{minutes:02d} hours after the start")
elif -30 <= difference <= 0:  # Студентът е навреме
    print("On time")
    if difference != 0:  # Ако има разлика, покажи минутите
        print(f"{abs(difference)} minutes before the start")
else:  # Студентът е подранил
    print("Early")
    difference = abs(difference)
    if difference < 60:
        print(f"{difference} minutes before the start")
    else:
        hours = difference // 60
        minutes = difference % 60
        print(f"{hours}:{minutes:02d} hours before the start")

# hour_exam = int(input())
# minutes_exam= int(input())
# hour_arrive = int(input())
# minutes_arrive = int(input())
#
# all_minutes_arrive=hour_arrive*60+minutes_arrive
# all_minutes_exam=hour_exam*60+minutes_exam
#
# if all_minutes_arrive>all_minutes_exam:
#     print("Late")
#     if all_minutes_arrive-all_minutes_exam<60:
#         print(f"{all_minutes_arrive-all_minutes_exam} minutes after the start" )
#     else:
#         hours = (all_minutes_arrive-all_minutes_exam)//60
#         minutes = (all_minutes_arrive-all_minutes_exam)%60
#         if minutes<10:
#             print(f"{hours}:0{minutes} hours after the start")
#         else:
#             print(f"{hours}:{minutes} hours after the start")
#
# else:
#
#     hours = (all_minutes_exam - all_minutes_arrive) // 60
#     minutes = (all_minutes_exam - all_minutes_arrive) % 60
#     if all_minutes_exam-all_minutes_arrive<=30:
#         print("On time")
#
#         print(f"{all_minutes_exam-all_minutes_arrive} minutes before the start")
#
#     else:
#         print("Early")
#         if hour_exam==hour_arrive:
#                 if minutes<10:
#                     print(f"0{minutes} minutes before the start" )
#                 else:
#                     print(f"{minutes} minutes before the start")
#         else:
#             if minutes < 10:
#                 print(f"{hours}:0{minutes} hours before the start")
#             else:
#                 print(f"{hours}:{minutes} hours before the start")


# if hour_arrive==hour_exam:
#
#     if minutes_arrive>minutes_exam:
#         print("Late")
#         print(f"{minutes_arrive-minutes_exam} minutes after the start" )
#     else:
#         if minutes_exam-minutes_arrive <=30:
#             print("On time")
#             print(f"{minutes_exam-minutes_arrive} minutes before the start" )
#         else:
#             print("Early")
#             print(f"{minutes_exam - minutes_arrive} minutes before the start")
#
# elif hour_arrive>hour_exam:
#     print("Late")
#     all_minutes_arrive = hour_arrive*60+minutes_arrive
#     all_minutes_exam = hour_exam* 60+minutes_arrive
#
# else:
