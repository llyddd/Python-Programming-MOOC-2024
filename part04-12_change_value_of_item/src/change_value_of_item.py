# Write your solution here
lists = [1,2,3,4,5]
while True:
  
    index = int(input("Index: "))
    if index == -1:
        break
    else:
        new_value = int(input("New Value: "))
        lists[index] = new_value
        print(lists)
    