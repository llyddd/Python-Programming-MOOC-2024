# write your solution here
def main():
    if True:
    # this is never executed
        student_info = input("Student information: ")
        exercise_data = input("Exercises completed: ")
        exam_points = input("Exam points: ")
    else:
    # hard-coded input
        student_info = "students1.csv"
        exercise_data = "exercises1.csv"
        exam_points = "exam_points1.csv"

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

    exam_pts = {}

    with open(exam_points) as new_file:
        for line in new_file:
            parts = line.split(';')
            if parts[0] == "id":
                continue
            exam_pts[parts[0]]  = int(parts[1]) + int(parts[2]) + int(parts[3]) 


    for id, names in student.items():
        if id in exercise:
            
            exercise_id = exercise[id]
            exercise_result = calculate_points(exercise_id)
                

            exam_pts_result = exam_pts[id]
            total = exercise_result + exam_pts_result
            
            average = grade(total)
            print(f"{names} {average}")

def calculate_points(completed_exercises, total_exercises=40):
    percentage_completed = (completed_exercises / total_exercises) * 100
    points = min(int(percentage_completed // 10), 10)
    return points

def grade(points):
    boundary = [0, 15, 18, 21, 24, 28]
    for i in range(5, -1, -1):
        if points >= boundary[i]:
            return i

main()