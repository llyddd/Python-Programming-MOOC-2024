# Write your solution here
def read_input(prompt: str, lower_limit: int, upper_limit: int):

    while True:
        try:
            number = int(input(prompt))
            if number > lower_limit and number < upper_limit:
                return number
            
            print(f"You must type in an integer between {lower_limit} and {upper_limit}")
        except ValueError:
            print(f"You must type in an integer between {lower_limit} and {upper_limit}")







if __name__ == "__main__":
    number = read_input("Please type in a number: ", 1, 5)
    print("You typed in:", number)