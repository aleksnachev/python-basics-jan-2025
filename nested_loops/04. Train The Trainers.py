n = int(input())
all_presentations_sum = 0
all_presentations_count = 0

command = input()

while command != "Finish":
    presentation_name = command
    grades_sum = 0
    grades = 0
    while grades < n:
        now_grade = float(input())
        grades_sum += now_grade
        all_presentations_sum += now_grade
        all_presentations_count += 1
        grades += 1
    average_grade = grades_sum / grades
    print(f"{presentation_name} - {average_grade:.2f}.")
    command = input()

print(f"Student's final assessment is {(all_presentations_sum / all_presentations_count):.2f}.")
