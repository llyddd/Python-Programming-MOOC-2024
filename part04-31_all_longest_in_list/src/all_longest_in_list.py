# Write your solution here

def all_the_longest(list):

    length_storage = []
    longest_storage = []
    i = 0
    o = 0
    
    while i < len(list):
        length_storage.append (len(list[i]))
        i+=1
    
    maximum = max(length_storage)
        
    while  o < len(list):    
        if len(list[o]) == maximum:
            longest_storage.append (list[o])
        o +=1
    return longest_storage
            
if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result)