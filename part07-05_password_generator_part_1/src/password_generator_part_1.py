# Write your solution here
from random import randint
from string import ascii_lowercase



def generate_password(length: int):
    ascii = []
    for char in ascii_lowercase:
        print(char)
        ascii.append(char)
    password = ""

    for i in range(length):
        result = randint(0, len(ascii)-1)
        password += ascii[result]
    return password

if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8))
 