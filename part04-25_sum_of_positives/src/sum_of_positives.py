# Write your solution here

def sum_of_positives(list):
    i = 0
    result = 0
    positive = [num for num in list if num > 0]
    while i < len(positive):
        result += positive[i]
        i+=1
    return result

  
    
if __name__ == "__main__":
    my_list = [1, -2, 3, -4, 5] 
    result = sum_of_positives(my_list)
    print("The result is", result)

