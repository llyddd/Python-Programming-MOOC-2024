# Write your solution here
def read(search_term):
    with open("diary.txt") as read_file:
        for line in read_file:
            if search_term in line:
                print(line)
def create(finnish, english):
    with open("diary.txt", "a") as add_file:
        add_file.write(f"{finnish} - {english}\n")

def main():
    
    while True:
        print("1 - Add word, 2 - Search, 3 - Quit")
        function = int(input("Function: "))

        if function == 1:
            finnish = input("The word in Finnish: ")
            english = input("The word in English: ")
            create(finnish, english)
            print("Dictionary entry added")
          
        elif function == 2:
            search = input("Search term: ")
            read(search)
           
        elif function == 3:
            print("Bye!")
            break

main()