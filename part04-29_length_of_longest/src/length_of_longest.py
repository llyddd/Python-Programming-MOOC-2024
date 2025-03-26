# Write your solution here

def length_of_longest(list):
    i = 0
    lenght_list = []
    while i < len(list):
        lenght_list.append (len(list[i]))
        i += 1
    
    result = max(lenght_list)
    return result


if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = length_of_longest(my_list)
    print(result)