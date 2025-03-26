import urllib.request
import json
import ssl # add this library to your import section
import math 

def retrieve_all():
    # add the following line to the beginning of all your functions
    context = ssl._create_unverified_context()
    request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses", context=context)
    read = request.read()
    data = json.loads(read)
   
    
    list_stats = []
    for items in data:
        exercise_total = 0
        if items["enabled"] == True:
            for key, value in items.items():
                
                if key == "exercises":
                    for num in value:
                        exercise_total += num
               
            
            stats = items["fullName"], items["name"], items["year"], exercise_total
            list_stats.append(stats)
    #print(list_stats)       
    return list_stats
 
def retrieve_course(course_name: str):
    context = ssl._create_unverified_context()
    url = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"
    request = urllib.request.urlopen(url, context=context)
    read = request.read()
    data = json.loads(read)


    student_count = []
    week_count = 0 #>
    hours_total = 0 #>
    exercise_total = 0 #>
    stats = {}

    for key, value in data.items():

        access = data[key]
        hours_total += access["hour_total"]
        student_count.append(access["students"])
        exercise_total += access["exercise_total"]
        week_count += 1
   
    max_student = max(student_count) #>
    hours_average = math.floor(hours_total/max_student) #>
    exercise_average = math.floor(exercise_total/max_student) #>
    stats["weeks"] = week_count
    stats["students"] = max_student
    stats["hours"] = hours_total
    stats["hours_average"] = hours_average
    stats["exercises"] = exercise_total
    stats["exercises_average"] = exercise_average

    return stats

if __name__ == "__main__":
    retrieve_course("docker2019")            
    retrieve_all()