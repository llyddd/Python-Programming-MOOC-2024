# Write your solution here
from datetime import datetime,timedelta
def read_start():
    list = []
    test = {}
    with open("start_times.csv") as read_file:
        for line in read_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            name = parts[0]
            hours_min = parts[1]
            list.append([name, hours_min])
            test[name] = hours_min
    return test

def read_submissions():
    list = []
    test = {}
    with open("submissions.csv") as read_file:
        for line in read_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            name = parts[0]
            task = parts[1]
            points = parts[2]
            hours_min = parts[3]
            list.append([name, task, points, hours_min]) 
            #test[name] = {"task":task, "points": points,"hours_min":hours_min}
    
    return list


def cheaters():
    start_time_dict = read_start()
    submissions_time_list = read_submissions()
    result = []


    for i in range(len(submissions_time_list)):
        for x in range(len(submissions_time_list[i])):
            #print(submissions_time_list[i][0])
            if submissions_time_list[i][0] in start_time_dict:
                sub_time = submissions_time_list[i][3]
                
                submission_time = datetime.strptime(str(sub_time),"%H:%M") 
                strt_time = datetime.strptime(str(start_time_dict[submissions_time_list[i][0]]),"%H:%M") 

                time_result = submission_time -  strt_time
                if time_result > timedelta(hours=3) and submissions_time_list[i][0] not in result:
                    result.append(submissions_time_list[i][0])

    return result


def final_points():
    start_time_dict = read_start()
    submission_time = read_submissions()
    cheater_res = cheaters()
    task_dict = {}

    
    for start_name in start_time_dict: #extracting items from submissions.csv using the names on start_times.csv
        
        for sub_name, task, points, time in submission_time:
            if start_name == sub_name:
                if sub_name not in task_dict:
                    task_dict[start_name] = {}

                if task not in task_dict[start_name]:
                    task_dict[start_name][task] = []
                #print(start_name)
                task_dict[start_name][task].append((int(points),time))

    task_max = {}
    for key, value in task_dict.items(): #extracting the time and checking if it is more than three hours then passing the task and points if it below three hours
        
        for sub_key, sub_value in value.items():
            total_points = 0
            for points,time in sub_value:
               
                task_time = datetime.strptime(str(time), "%H:%M")
                strt_time = datetime.strptime(start_time_dict[key], "%H:%M")
                time_result = task_time -  strt_time
                if time_result < timedelta(hours=3):

                    total_points += points
                    if key not in task_max:
                        
                        task_max[key] = {}
                    if sub_key not in task_max[key]:
                        task_max[key][sub_key] = []    
                    task_max[key][sub_key].append(points)
    print(task_max)
                

    task_total = {}
    for key, value in task_max.items(): #finding the max values if there are multiple submissions in one task
        for sub_key, sub_value in value.items():
  
            maximum = max(sub_value)
            
            if key not in task_total:
                task_total[key] = []
            task_total[key].append(maximum)
    
    final_result = {}

    for key, value in task_total.items(): #getting the total points for each person
        total =0 
        for num in value:
            total += num
        final_result[key] = total

    return final_result
   
if __name__ == "__main__":
    cheaters()
    final_points()
