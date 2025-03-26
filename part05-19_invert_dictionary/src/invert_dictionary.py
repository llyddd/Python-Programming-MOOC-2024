def invert(dictionary: dict):
    # Create a temporary dictionary to store inverted pairs
    temp = {}
    
    # Iterate through the original dictionary
    for key, value in dictionary.items():
        # Store the inverted key-value pairs in the temporary dictionary
        temp[value] = key
    
    # Clear the original dictionary
    dictionary.clear()
    
    # Update the original dictionary with the inverted pairs
    dictionary.update(temp)
        

if __name__ == "__main__":
    s = {1: 10, 2: 20, 3: 30}
    print(s)  # Before: {1: 10, 2: 20, 3: 30}
    invert(s)
    print(s)  # After: {10: 1, 20: 2, 30: 3}