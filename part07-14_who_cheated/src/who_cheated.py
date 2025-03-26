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

if __name__ == "__main__":
    cheaters()
