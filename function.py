
def calculate_total(marks):
    return sum(marks.values())
def calculate_average(marks):
    return round(calculate_total(marks)/len(marks),2)
def get_grade(average):
    if calculate_average(average)>=90:
        return "A"
    elif calculate_average(average)>=75:
        return "B"
    elif calculate_average(average)>=60:
        return "C"
    elif calculate_average(average)>=40:
        return "D"
    else:
        return "Fail"

def check_results(marks,pass_mark=40):
    res = lambda marks,pass_mark:"Pass" if pass_mark>=40 else "Fail"
    return res(marks,pass_mark)


def student_summary(student):
    marks = student["marks"]
    return{
        "name": student["name"],
        "total": calculate_total(marks),
        "average":calculate_average(marks),
        "grade":get_grade(marks),
        "result":check_results(marks)


    }
    
def update_marks(data, student_id, **changes):
    """Updates specific subject marks for a student if the ID exists."""
    if student_id not in data:
        return False
    for subject, mark in changes.items():
        data[student_id]["marks"][subject] = mark
    return True

def add_student(data, student_id, name, **marks):
    """Adds a new student if the ID doesn't already exist."""
    if student_id in data:
        return False
    data[student_id] = {"name": name, "marks": marks}
    return True

def remove_student(data, student_id):
    """Removes a student by ID if present."""
    if student_id not in data:
        return False
    del data[student_id]
    return True

def print_report(data):
    """Prints the sorted report table by average (highest first)."""
    sorted_students = []
    for s_id, s in data.items():
        avg = calculate_average(s["marks"])
        sorted_students.append((avg, s_id))
    

    sorted_students.sort(reverse=True)
    
    print(f"{'ID':<6}{'Name':<10}{'Total':<10}{'Avg':<8}{'Grade':<8}{'Result'}")
    print("-" * 50)
    
    for avg, s_id in sorted_students:
        student = data[s_id]
        name = student["name"]
        total = calculate_total(student["marks"])
        grade = get_grade(student["marks"])
        result = check_results(student["marks"])
        print(f"{s_id:<6}{name:<10}{total:<10}{avg:<8.2f}{grade:<8}{result}")

def class_statistics(data, *subjects):
    """Returns class statistics including topper, pass percentage, and subject averages."""
    if not data:
        return {"topper": None, "pass_percentage": 0.0, "subject_averages": {}}
    

    topper_id = max(data, key=lambda s_id: calculate_average(data[s_id]["marks"]))
    topper_name = data[topper_id]["name"]
    

    passed_count = 0
    for s in data.values():
        if check_results(s["marks"]) == "Pass":
            passed_count += 1
    pass_percentage = round((passed_count / len(data)) * 100, 1)
    
 
    all_subjects = set()
    for s in data.values():
        for sub in s["marks"].keys():
            all_subjects.add(sub)
            
    target_subjects = subjects if subjects else all_subjects
    
    subject_averages = {}
    for sub in target_subjects:
        marks_list = []
        for s in data.values():
            if sub in s["marks"]:
                marks_list.append(s["marks"][sub])
        if marks_list:
            subject_averages[sub] = round(sum(marks_list) / len(marks_list), 1)
            
    return {
        "topper": topper_name,
        "pass_percentage": pass_percentage,
        "subject_averages": subject_averages
    }