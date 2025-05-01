name = input()
average_grade = 0
executed_count = 0
years_count = 0
while years_count < 12:
    cur_year_grade = float(input())

    if cur_year_grade < 4:
        executed_count += 1

        if executed_count > 1:
            print(f"{name} has been excluded at {years_count + 1} grade")
            break
        continue

    years_count += 1
    average_grade += cur_year_grade



else:
    print(f"{name} graduated. Average grade: {(average_grade / years_count):.2f}")
