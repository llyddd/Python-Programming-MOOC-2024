# Write your solution here
def same_chars(string, num1, num2):
    
    length = len(string)
    
    if num1 >= length or num2 >= length :
        return False
    else:
        x = string [num1]
        y = string [num2]
        if x == y:
            return True
        else:
            return False
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("abc",0, 3))