
# write your solution here
def read_course_info(course_info):
    course = {}
    with open(course_info) as read_file:
        for line in read_file:
            line = line.replace("\n", "")
            parts = line.split(": ")
            header = parts[0]
            values = parts[1]
            course[header] = values
    return course
def read_student_info(student_info):
    student = {}
    with open(student_info) as new_file:
        for line in new_file:
            parts = line.split(';')
            if parts[0] == "id":
                continue
            
            student[parts[0]] = f"{parts[1]} {parts[2]}".strip()
    return student
def read_exercise_info(exercise_data):
    exercise = {}
    with open(exercise_data) as new_file:
        for line in new_file:
            parts = line.split(';')
            if parts[0] == "id":
                continue
            exercise[parts[0]] = int(parts[1]) + int(parts[2]) + int(parts[3]) + int(parts[4]) + int(parts[5]) + int(parts[6]) + int(parts[7])
    return exercise

def read_exam_points(exam_points): 
    exam_pts = {}
    with open(exam_points) as new_file:
        for line in new_file:
            parts = line.split(';')
            if parts[0] == "id":
                continue
            exam_pts[parts[0]]  = int(parts[1]) + int(parts[2]) + int(parts[3]) 
    return exam_pts

def add_results_csv(result: list):
        with open("results.csv", "w") as write_file:
            for item in result:
                line = ""
                for value in item:
                    line += f"{value};"
                line = line[:-1]
                write_file.write(line+"\n")

def add_result_txt(result: list):
        with open("results.txt", "w") as add_file:
            for item in result:
                add_file.write(f"{item}\n")          


def calculate_points(completed_exercises, total_exercises=40):
    percentage_completed = (completed_exercises / total_exercises) * 100
    points = min(int(percentage_completed // 10), 10)
    return points

def grade(points):
    boundary = [0, 15, 18, 21, 24, 28]
    for i in range(5, -1, -1):
        if points >= boundary[i]:
            return i
        
def main():
    if True:
    # this is never executed
        student_info = input("Student information: ")
        exercise_data = input("Exercises completed: ")
        exam_points = input("Exam points: ")
        course_info = input("Course information: ")
    else:
    # hard-coded input
        student_info = "students1.csv"
        exercise_data = "exercises1.csv"
        exam_points = "exam_points1.csv"
        course_info = "course1.txt "

    course = {}
    course = read_course_info(course_info)
    student = {}
    student = read_student_info(student_info)

    exercise = {}
    exercise = read_exercise_info(exercise_data)
    exam_pts = {}
    exam_pts = read_exam_points(exam_points)
    
    cname = "name"
    exec_nbr = "exec_nbr"
    exec_pts = "exec_pts."  
    exm_pts = "exm_pts."  
    tot_pts = "tot_pts." 
    cgrade = "grade"
    result_csv = []
    result_txt = []
    #print(f"{cname:<30}{exec_nbr:<10}{exec_pts:<10}{exm_pts:<10}{tot_pts:<10}{cgrade:<10}")
    temp = ""
    for name, values in course.items():
        temp += f"{values}, "
    temp = temp[:-2] + " credits"   
    equal = len(temp) * "="
    result_txt.append(temp)
    result_txt.append(equal)
    result_txt.append((f"{cname:<30}{exec_nbr:<10}{exec_pts:<10}{exm_pts:<10}{tot_pts:<10}{cgrade:<10}"))
    
    for id, names in student.items():
        
        if id in exercise:
            
            exercise_id = exercise[id]
            exercise_result = calculate_points(exercise_id)
            exam_pts_result = exam_pts[id]
            total = exercise_result + exam_pts_result
            average = grade(total)
            #print(f"{names:<30}{exercise_id:<10}{exercise_result:<10}{exam_pts_result:<10}{total:<10}{average:<10}")
            result_txt.append((f"{names:<30}{exercise_id:<10}{exercise_result:<10}{exam_pts_result:<10}{total:<10}{average:<10}"))
            result_csv.append((id,names, average))

    add_results_csv(result_csv)
    add_result_txt(result_txt)

main()