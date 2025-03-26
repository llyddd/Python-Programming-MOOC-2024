# write your solution here

def student_database():
    if True:
    # this is never executed
        student_info = input("Student information: ")
        exercise_data = input("Exercises completed: ")
    else:
    # hard-coded input
        student_info = "students1.csv"
        exercise_data = "exercises1.csv"

    student = {}
    with open(student_info) as new_file:
        for line in new_file:
            parts = line.split(';')
            if parts[0] == "id":
                continue
            
            student[parts[0]] = f"{parts[1]} {parts[2]}".strip()

    exercise = {}
    with open(exercise_data) as new_file:
        for line in new_file:
            parts = line.split(';')
            if parts[0] == "id":
                continue
            exercise[parts[0]] = int(parts[1]) + int(parts[2]) + int(parts[3]) + int(parts[4]) + int(parts[5]) + int(parts[6]) + int(parts[7])

    for id, names in student.items():
        if id in exercise:
            result = exercise[id]
            print(f"{names} {result}")

    

student_database()