from function import calculate_total,calculate_average,get_grade,check_results,student_summary,update_marks,add_student,remove_student,print_report,class_statistics

students = {
"S101": {"name": "Anu", "marks": {"Python": 88, "Maths": 76, "Stats": 92}},
"S102": {"name": "Binu", "marks": {"Python": 45, "Maths": 38, "Stats": 52}},
"S103": {"name": "Cathy", "marks": {"Python": 95, "Maths": 91, "Stats": 89}},
"S104": {"name": "Dev", "marks": {"Python": 60, "Maths": 72, "Stats": 55}},
"S105": {"name": "Esha", "marks": {"Python": 72, "Maths": 65, "Stats": 80}},
}
print(f" Task 1 : One student")
print(f"Name is {students["S101"]["name"]} , 'total': {calculate_total(students["S101"]["marks"])}")
print(f"Average is {calculate_average(students["S101"]["marks"])}")
print(f"Grade is {get_grade(students['S101']["marks"])}")
print(f"Result is {check_results(students['S101']['marks'])}: ")

print("\nTask 2 : Student Summary Dictionary")
summary = student_summary(students["S101"])
print(summary)

print("Task 3: Update marks")
print(update_marks(students, "S102", Maths=55))
print(update_marks(students, "S999", Maths=50))
corrections = {"Python": 50, "Stats": 58}
print(update_marks(students, "S102", **corrections))
print(student_summary(students["S102"]))
print()

print("Task 4: Add student")
print(add_student(students, "S106", "Farhan", Python=70, Maths=35, Stats=74))
print(add_student(students, "S101", "Zara", Python=50, Maths=50, Stats=50))
print(students["S106"])
print()

print("Task 5: Remove student")
print(remove_student(students, "S104"))
print(remove_student(students, "S104"))
print(len(students))
print()

print("Task 6: Final report and statistics")
print_report(students)
stats = class_statistics(students)
print(f"Topper: {stats['topper']}")
print(f"Pass percentage: {stats['pass_percentage']}")
print(f"Subject averages: {stats['subject_averages']}")

sub_stats = class_statistics(students, "Python", "Stats")
print(f"Python and Stats only: {sub_stats['subject_averages']}")