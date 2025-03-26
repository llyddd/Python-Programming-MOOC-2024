# Write your solution here

def no_vowels(string):
    vowels = ["a", "e", "i", "o", "u"]
    storage = ""

    for i in string:
        if i not in vowels:
            storage += i  
    return storage




if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))