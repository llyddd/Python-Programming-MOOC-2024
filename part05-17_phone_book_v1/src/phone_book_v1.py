# Write your solution here

phonebook = {}
def search():
    name = input("name: ")

    if name in phonebook:
        
        print(phonebook[name])
    else:
        print("no number")
    

def add():
    name = input("name: ")
    number = input("number: ")

    phonebook[name] = number
    print("ok!")



while True:
    command = int(input ("command (1 search, 2 add, 3 quit)"))

    if command == 1:
        search()
    elif command == 2:
        add()
    elif command == 3:
        print("quitting...")
        break

