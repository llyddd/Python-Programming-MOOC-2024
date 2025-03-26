# Write your solution here
from datetime import datetime, timedelta

def main():

    if True:
        file_result = input("Filename: ")
        starting = input("Starting date: " )
        days_to_count = int(input("How many days: "))
    else:
        file_result = "late_june.txt"
        #starting = input("Starting date: " )
        starting = "29.06.2020"
        starting_date = datetime.strptime(starting, "%d.%m.%Y")
        days_to_count = 3

    #Creating object, from string to datetime
    starting_date = datetime.strptime(starting, "%d.%m.%Y")
    
    #Storing of screen date and time
    screen_time = []

    total_minutes = 0

    #loop to get each screen time based on the day count
    ctr = 0
    while ctr < days_to_count:
        
        #adding days to starting date up to the last day and transforming it to string format 
        screen_date = starting_date + timedelta(days= ctr) 
        screen_date = screen_date.strftime("%d.%m.%Y")

        #Input of time for each day and replacing spaces to slash, then joining the screen date and the time
        time_input = input(f"Screen time {screen_date}: ")
        time_slash = time_input.replace(" ","/")
        time = f"{screen_date}: {time_slash}"
        screen_time.append(time)
       
       #splitting the time so it can be calculated for total minutes
        parts = time_input.split(" ")
        minute_1 = int(parts[0])
        minute_2 = int(parts[1]) 
        minute_3 = int(parts[2])
        total_minutes += (minute_1 + minute_2 + minute_3)

        ctr += 1
    
    result = []
    average_minutes = float(total_minutes / days_to_count)    
    
    time_period_result = f"Time period: {starting_date.strftime("%d.%m.%Y")}-{screen_date}"
    total_result = f"Total minutes: {total_minutes}"
    average_result = f"Average minutes: {average_minutes:.1f}"
    

    #Added first the header results and use a loop to add the screen time, 
    #so that when i pass it to create, it is one list
    result.append(time_period_result)
    result.append(total_result)
    result.append(average_result)
    for item in screen_time:
        result.append(item)

    create(file_result, result)

def create(filename: str, result: list):
    
    with open(filename, "w") as add_file:
        
        for line in result:
            add_file.write(line+"\n")

    print(f"Data stored in file {filename}")  


main()




