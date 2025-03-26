# Write your solution here
def remove_smallest(numbers: list):
    
    sorter = []

    for i in numbers:
        sorter.append(i)
    sorter.sort()
    
    smallest_item = sorter[0]
   
    for item in numbers:
        
        if item == smallest_item:
            numbers.remove(item)
            



if __name__ == "__main__":
    numbers = [2, 3, 5, 6]
    remove_smallest(numbers)
    print(numbers)