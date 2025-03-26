# Write your solution here
def oldest_person(people: list):
    
    temp_list = []
    temp_year = []
    for date in people:
        temp_list.append(date)
    print(temp_list)
    i = 0
    while i < len(temp_list):
        temp_year.append(temp_list[i][1])
        i += 1
    
    older = min(temp_year)

    o = 0
    while o < len(temp_list):
        if older == temp_list[o][1]:
            return temp_list[o][0]
        o += 1
 
if __name__ == "__main__":
    p1 = ("Arthur", 1977)
    p2 = ("Emily", 2014)
    people = [p1, p2]

    print(oldest_person(people))