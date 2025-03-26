# Write your solution here
def read():
    with open("diary.txt") as read_file:
        for line in read_file:
            print(line)
def add(text):
    with open("diary.txt", "a") as add_file:
        add_file.write(f"{text}\n")
def main():
    
    while True:
        print("1 - add an entry, 2 - read entries, 0 - quit")    
        func = int(input("Function: "))
        
        if func == 1:
            text = input("Diary entry:")
            add(text)
            print("Diary saved")
        elif func == 2:
            read()
        elif func == 0:
            print("Bye now!")
            break


main()