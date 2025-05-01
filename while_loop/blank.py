# ungrateful_grades = int(input())
# grade_sum = 0
# all_exercises = 0
# ungrateful_grades_counter = 0
# last_exercise = ""
# while True:
#     name_exercise = input()
#     if name_exercise == "Enough":
#         average_score = grade_sum / all_exercises
#         print(f"Average score: {average_score:.2f}")
#         print(f"Number of problems: {all_exercises}")
#         print(f"Last problem: {last_exercise}")
#         break
#     last_exercise = name_exercise
#     grade = int(input())
#     if grade <= 4:
#         ungrateful_grades_counter += 1
#
#         if ungrateful_grades_counter == ungrateful_grades:
#             print(f"You need a break, {ungrateful_grades_counter} poor grades.")
#
#     grade_sum += grade
#     all_exercises += 1
#
# needed_money = float(input())
# money = float(input())
# spend_counter = 0
# days_counter = 0
#
# while True:
#     command = input()
#     sum = float(input())
#
#     if command == "spend":
#         spend_counter += 1
#         if money - sum < 0:
#             money = 0
#         else:
#             money = money - sum
#
#         if spend_counter == 5:
#             print("You can't save the money.")
#             print(days_counter+1)
#             break
#     elif command == "save":
#         money += sum
#         spend_counter = 0
#     days_counter += 1
#
#     if money >= needed_money:
#         print(f"You saved the money for {days_counter} days.")

print(120//100)