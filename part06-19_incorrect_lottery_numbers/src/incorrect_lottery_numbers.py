def read():
    result_list = []  # Initialize an empty list to store processed data
    
    # Open the file "lottery_numbers.csv" in read mode
    with open("lottery_numbers.csv") as read_file:
        # Loop through each line in the file
        for line in read_file:
            line = line.strip()  # Remove leading/trailing whitespaces and newline characters

            parts = line.split(";")  # Split the line using ";" as the delimiter

            # Ensure the line contains at least two parts (week number and lottery numbers)
            if len(parts) < 2:
                continue  # Skip to the next line if the format is incorrect
            
            week_part = parts[0]  # Extract the week number (first part of the split line)
            #print(week_part)
            int_part = parts[1]  # Extract the lottery number section (second part)

            #week = week_part.split(" ")
            integers = int_part.split(",")  # Split the lottery numbers using "," as the delimiter
          
            # Convert the extracted numbers from strings to integers
            try:
                numbers = [num for num in integers]
            except ValueError:
                #print(f"Skipping line: {line} (Non-integer values found)")
                continue  # Skip this line if conversion fails

            # Append the processed week number and lottery numbers as a list into result_list
            result_list.append([week_part] + numbers)
    #print(result_list)

    return result_list  # Return the final list containing all valid data


def filter_incorrect():
    data_list = []
    data_list = read()
    remove_item = []

    no_error = False
    corrected = []
    for i in range(len(data_list)):  # Loop through each week's data
        temp = []
        no_error = False  # Reset per week entry
        has_error = False  # Track if an entry has already been marked

        for x in range(len(data_list[i])):  # Loop through each element in the week's data
            
            if data_list[i][x] == data_list[i][0]:  # Check if it's the week identifier
                parts = data_list[i][x].split(" ")
                if len(parts) > 1 and parts[1].isdigit():
                    no_error = True
                else:
                    if not has_error:  # Prevent duplicate append and print
                        remove_item.append(data_list[i])
                        #print("The week number is incorrect:", data_list[i])
                        has_error = True
            else:
                
                if no_error:  # Proceed only if the week number was valid
                    
                    try: 
                        convert = int(data_list[i][x])
                        data_list[i][x] = convert     
                    except:
                        remove_item.append(data_list[i]) 
                        #print("One or more numbers are not correct: ", data_list[i]) 
                        has_error = True  

                    if len(data_list[i]) < 8 and not has_error:
                        remove_item.append(data_list[i])
                        #print("Too few numbers:", data_list[i])
                        has_error = True  # Mark to prevent multiple prints

        #Check if there are too small or large number
                    if data_list[i] not in remove_item and not has_error: 
                        if data_list[i][x] < 1 or data_list[i][x] > 39:
                            remove_item.append(data_list[i])
                            #print("The numbers are too small or large: ", data_list[i])
                            has_error = True  # Mark to prevent multiple prints
                    
                    if len(data_list[i]) != len(set(data_list[i]))and not has_error:
                        remove_item.append(data_list[i])
                        #print("The same number appears twice: ", data_list[i])
                        has_error = True 
        
        
    for data in data_list:

        if data not in remove_item: 
            corrected.append(data)
    add_correct(corrected)
def add_correct(data_list: list):
    i = 0 
    with open("correct_numbers.csv", "w", newline="") as write_file:  # FIXED
        for item in data_list:
            line = ""
            
            for value in item:
                if value == data_list[i][0]:
                    line += f"{value};"
                else:
                    line += f"{value},"
            line = line[:-1]
            write_file.write(line + "\n")
            i += 1

    
  
if __name__ == "__main__":

    filter_incorrect()