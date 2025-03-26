# write your solution here

def converter():
    numbers = []  # Create an empty list to store the matrix
    
    with open("matrix.txt") as new_file:
        for line in new_file:  
            values = line.strip().split(",")  # Remove \n and split by comma
            row = [int(value) for value in values]  # Convert to integers
            numbers.append(row)  # Add row to the list
    
    return numbers  # Return the list



    
def matrix_max():
    list_max_temp = []
    list_max_temp = converter()
    list_max = []
    list_final = []

    for row in list_max_temp:
        for value in row:
            list_max.append(value)
    return max(list_max)


def matrix_sum(): 
    list_sum = []
    list_sum = converter()
    list_sum_temp = []
    
    
    for row in list_sum:
        m_sum = 0
        for value in row:
            m_sum += value
        list_sum_temp.append(m_sum)

    i = 0
    result = 0
    while i < len(list_sum_temp):
        result += list_sum_temp[i]
        i+=1
    return result


       
def row_sums():
    list_row_sum = []
    list_row_sum = converter()
    list_temp = []
    for row in list_row_sum:
        row_sum = 0
        for value in row:
            row_sum += value
        list_temp.append(row_sum)
        
    return list_temp

    



if __name__ == "__main__": 
    matrix_sum()
    matrix_max()
    row_sums()
