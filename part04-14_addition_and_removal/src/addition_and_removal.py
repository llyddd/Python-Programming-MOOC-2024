# Write your solution here
my_list = []
i = 0
while True:
    
    
    print(f"The list is now {my_list}")
    choice = input("a(d)d, (r)emove or e(x)it: ")

    if choice == "d":
        i += 1
        my_list.append(i)
        
    elif choice == "r":
        i -= 1
        my_list.pop(i)
        
        
    elif choice == "x":
        print ("Bye!")
        break
        