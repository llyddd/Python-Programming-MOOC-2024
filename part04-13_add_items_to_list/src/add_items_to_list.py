# Write your solution here
item_list = []
times = int(input("How many items: "))
i = 1
while i <= times:
    item = int(input(f"Item {i}: "))
    item_list.append(item)
    i += 1 
print (item_list)