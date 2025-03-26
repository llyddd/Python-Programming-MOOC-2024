# Write your solution here

my_list = []

while True:
    string = input("Word: ")
    
    if string not in my_list:
        my_list.append(string) 
        ctr = len(my_list)
    else:
        break 
print (f"You typed in {ctr} different words")