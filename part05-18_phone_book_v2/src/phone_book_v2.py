phonebook = {}

def search():
    name = input("name: ")
    if name in phonebook:
        for number in phonebook[name]:  # Print all numbers for the name
            print(number)
    else:
        print("no number")     

def add():
    name = input("name: ")
    number = input("number: ")
    
    if name in phonebook:  # If name exists, append to existing list
        phonebook[name].append(number)
    else:  # If name doesn't exist, create new list with number
        phonebook[name] = [number]
    print("ok!")

while True:
    command = int(input("command (1 search, 2 add, 3 quit): "))

    if command == 1:
        search()
    elif command == 2:
        add()
    elif command == 3:
        print("quitting...")
        break