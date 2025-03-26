# Write your solution here
def factorials(n: int):
    my_dictionary = {}
    ctr = 1
    temp = 1
    while ctr <= n:
        
        temp = temp * ctr
        my_dictionary [ctr]  = temp
        ctr += 1
    return my_dictionary
    

        
      


if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])
    