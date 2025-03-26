# Write your solution here

def even_numbers(list):

    even = [num for num in list if num % 2 == 0]
    return even

  
    
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5] 
    result = even_numbers(my_list)
    print("original", my_list)
    print("new", result)

