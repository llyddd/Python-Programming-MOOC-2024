# Write your solution here
def list_of_stars(list):
    
    stars = list
    i = 0
    while i < len(list):
        print(f"{"*" * stars[i]}")
        i+=1


if __name__ == "__main__":
    
    list  = [3,7,1,1,2]
    print(list_of_stars(list))