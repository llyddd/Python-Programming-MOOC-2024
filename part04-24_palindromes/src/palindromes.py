# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
def palindromes(word):
    reversed_string = ""
    for i in range(len(word) - 1, -1, -1):
        reversed_string += word[i]
    reverse = reversed_string

    if reverse != word:
        return False
    else:
       return True
def main():
    while True:
        string = input("Please type in a palindrome: ")
    
        if palindromes(string):
            print(f"{string} is a palindrome!")
            break
        print("that wasn't a palindrome")

main()
   
