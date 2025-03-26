# Write your solution here
from datetime import datetime,timedelta

def main():

    #Current millennium year
    new_mill = 2000 

    #Input of user
    if True:
        day = int(input("Day: "))
        month = int(input("Month: "))
        year = int(input("Year: "))
    else:
        day = 1
        month = 1
        year = 2100
        # day = 1
        # month = 1
        # year = 1900
    

    #Getting the new millennium year
    new_millennium_year = (year//1000 +1)* 1000

    #Creating the object of datetime
    millennium_date = datetime(new_millennium_year, 1, 1)

    #If else for to check if they are already born or not
    if year < new_millennium_year and year < new_mill:
        result = (datetime(year,month,day) - millennium_date)*-1
        print(f"You were {(result.days-1)} days old on the eve of the new millennium.")
    elif year >= new_mill:
        print("You weren't born yet on the eve of the new millennium.")

    
    

    

main() 
